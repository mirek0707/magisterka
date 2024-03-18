import datetime
from fastapi import APIRouter, HTTPException
from database.db import books_collection
from models.book import BookModel, CreateBookModel

router = APIRouter(
    prefix="/books", tags=["books"], responses={404: {"description": "Not found"}}
)


@router.get("/{isbn}", response_description="Get one book", response_model=BookModel)
async def get_one_book(isbn: str):
    book = await books_collection.find_one({"isbn": isbn})
    if not book:
        raise HTTPException(status_code=404)
    return book


@router.get("", response_description="Get one book", response_model=list[BookModel])
async def get_books_per_page(
    page: int = 1,
    limit: int = 30,
    sort_by: str = "ratings_number",
    order: int = -1,
    release_year_from: int | None = None,
    release_year_to: int | None = None,
    author: str | None = None,
    publisher: str | None = None,
    genre: str | None = None,
):
    sort_by_list = BookModel.model_fields.keys()
    if sort_by not in sort_by_list or order not in [-1, 1]:
        raise HTTPException(status_code=400, detail="Wrong sorting parameters")
    if page <= 0 or limit <= 0:
        raise HTTPException(status_code=400, detail="Wrong pagination parameters")
    skip = page * limit - limit

    query = {}

    if release_year_from is not None and release_year_to is not None:
        from_date = datetime.datetime(release_year_from - 1, 12, 31, 12, 30, 30, 125000)
        to_date = datetime.datetime(release_year_to, 12, 31, 12, 30, 30, 125000)
        query["$or"] = [
            {"release_year": {"$gte": release_year_from, "$lte": release_year_to}},
            {"release_date": {"$gt": from_date, "$lte": to_date}},
        ]
    elif release_year_from is not None:
        from_date = datetime.datetime(release_year_from - 1, 12, 31, 12, 30, 30, 125000)
        query["$or"] = [
            {"release_year": {"$gte": release_year_from}},
            {"release_date": {"$gt": from_date}},
        ]
    elif release_year_to is not None:
        to_date = datetime.datetime(release_year_to, 12, 31, 12, 30, 30, 125000)
        query["$or"] = [
            {"release_year": {"$lte": release_year_to}},
            {"release_date": {"$lte": to_date}},
        ]

    if author:
        query["author"] = {"$regex": author, "$options": "i"}

    if publisher:
        query["publisher"] = {"$regex": publisher, "$options": "i"}

    if genre:
        query["genre"] = {"$regex": genre, "$options": "i"}

    books = (
        await books_collection.find(query)
        .sort({sort_by: order})
        .skip(skip)
        .limit(limit)
        .to_list(length=None)
    )
    return books


@router.post(
    "/ftsearch",
    response_description="Full-text search in description, title, original_title, author",
    response_model=list[BookModel],
)
async def full_text_search_book(query: str, num_of_books: int = 30):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter cannot be empty")

    if len(query) < 3:
        raise HTTPException(
            status_code=400, detail="Query parameter must have at least 3 characters"
        )

    projection = {"score": {"$meta": "textScore"}}
    query = f'"{query}"'
    books = await books_collection.find(
        {"$text": {"$search": query}}, projection=projection
    ).to_list(length=None)

    books = sorted(books, key=lambda x: x["score"], reverse=True)
    books = books[:num_of_books]

    return books


@router.post(
    "/search",
    response_description="Search by author, title or original_title",
    response_model=list[BookModel],
)
async def search_book(query: str, num_of_books: int = 5):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter cannot be empty")

    books = await books_collection.find(
        {
            "$or": [
                {"author": {"$regex": query, "$options": "i"}},
                {"original_title": {"$regex": query, "$options": "i"}},
                {"title": {"$regex": query, "$options": "i"}},
            ]
        }
    ).to_list(length=None)

    books = sorted(books, key=lambda x: x["ratings_lc_number"], reverse=True)
    books = books[:num_of_books]

    return books


@router.post("")
async def add_book(create_book_model: CreateBookModel):
    book = await books_collection.find_one({"isbn": create_book_model.isbn})
    if book is not None:
        raise HTTPException(
            status_code=409,
            detail=f"Book with ISBN: '{create_book_model.isbn}' already exist",
        )

    new_book = BookModel(
        **create_book_model.model_dump(),
        rating_lc=None,
        rating_gr=None,
        rating_tk=None,
        ratings_lc_number=None,
        ratings_gr_number=None,
        ratings_tk_number=None,
        rating=None,
        ratings_number=None,
    )
    result = await books_collection.insert_one(new_book.model_dump(exclude=["id"]))

    if result.inserted_id:
        return {"message": "Book added successfully!"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add book to database")
