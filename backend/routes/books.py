import datetime
import re
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from database.db import books_collection
from models.book import BookModel, CreateBookModel, UpdateBookModel
from pyisbn import Isbn
from utils.rating import ratingNumberSum, calculateRating
from bson.objectid import ObjectId, InvalidId
from utils.authentication import admin_dependency, user_dependency
from typing import Annotated

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={
        200: {"description": "OK"},
        201: {"description": "Record created"},
        400: {"description": "Bad request"},
        404: {"description": "Not found"},
        409: {"description": "Conflict, record already in database"},
        422: {"description": "Unprocessable content"},
        500: {"description": "Internal server error"},
    },
)


@router.get("/count", response_description="Get number of books")
async def get_books_count(
    _: user_dependency,
    release_year_from: int | None = None,
    release_year_to: int | None = None,
    author: str | None = None,
    publisher: str | None = None,
    genre: str | None = None,
):
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
        escaped_genre = re.sub(r"(\(|\))", r"\\\1", genre)
        query["genre"] = {"$regex": escaped_genre, "$options": "i"}

    count = await books_collection.count_documents(query)
    return {"count": count}


@router.get("/genres", response_description="Get all available genres")
async def get_all_genres(_: user_dependency):
    genres = await books_collection.distinct("genre")
    return {"genres": genres}


@router.get("/publishers", response_description="Get all available publishers")
async def get_all_publishers(_: user_dependency):
    unique_publishers = set()
    publishers = await books_collection.distinct("publisher")
    unique_publishers.update(publishers)
    return {"publishers": sorted(unique_publishers)}


@router.get("/authors", response_description="Get all available authors")
async def get_all_authors(_: user_dependency):
    unique_authors = set()
    authors = await books_collection.distinct("author")
    unique_authors.update(authors)
    return {"authors": sorted(unique_authors)}


@router.get("/years", response_description="Get min and max release years")
async def get_min_max_release_years(_: user_dependency):
    max_date = await books_collection.find_one(
        {}, {"release_date": 1}, sort=[("release_date", -1)]
    )

    min_date = await books_collection.find_one(
        {"release_date": {"$exists": True, "$ne": []}},
        {"release_date": 1},
        sort=[("release_date", 1)],
    )

    max_rel_year = await books_collection.find_one(
        {}, {"release_year": 1}, sort=[("release_year", -1)]
    )

    min_rel_year = await books_collection.find_one(
        {"release_year": {"$exists": True, "$ne": []}},
        {"release_year": 1},
        sort=[("release_year", 1)],
    )

    max_year = max(
        max(max_date["release_date"]).year, max(max_rel_year["release_year"])
    )
    min_year = min(
        min(min_date["release_date"]).year, min(min_rel_year["release_year"])
    )

    return {"max_year": max_year, "min_year": min_year}


@router.get(
    "/list",
    response_description="Get books by isbns list",
    response_model=list[BookModel],
)
async def get_books_by_isbn_list(
    _: user_dependency, isbn: Annotated[list[str], Query()] = None
):
    books = await books_collection.find({"isbn": {"$in": isbn}}).to_list(length=None)
    if not books:
        raise HTTPException(status_code=404)
    return books


@router.get(
    "/ftsearch",
    response_description="Full-text search in description, title, original_title, author",
    response_model=list[BookModel],
)
async def full_text_search_book(_: user_dependency, query: str, num_of_books: int = 30):
    if not query:
        raise HTTPException(status_code=422, detail="Query parameter cannot be empty")

    if len(query) < 3:
        raise HTTPException(
            status_code=422, detail="Query parameter must have at least 3 characters"
        )

    projection = {"score": {"$meta": "textScore"}}
    query = f'"{query}"'
    books = await books_collection.find(
        {"$text": {"$search": query}}, projection=projection
    ).to_list(length=None)

    books = sorted(books, key=lambda x: x["score"], reverse=True)
    books = books[:num_of_books]

    return books


@router.get(
    "/search",
    response_description="Search by author, title or original_title",
    response_model=list[BookModel],
)
async def search_book(_: user_dependency, query: str, num_of_books: int = 5):
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

    books = sorted(books, key=lambda x: x["ratings_number"], reverse=True)
    books = books[:num_of_books]

    return books


@router.get("/{isbn}", response_description="Get one book", response_model=BookModel)
async def get_one_book(isbn: str, _: user_dependency):
    # try:
    #     isbn_obj = Isbn(isbn)
    #     if not isbn_obj.validate():
    #         raise ValueError("ISBN is not valid")
    # except:
    #     raise HTTPException(status_code=422, detail="Not a valid ISBN")

    book = await books_collection.find_one({"isbn": isbn})
    if not book:
        raise HTTPException(status_code=404)
    return book


@router.get(
    "",
    response_description="Get books with pagination, sorting and filters",
    response_model=list[BookModel],
)
async def get_books_per_page(
    _: user_dependency,
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
        raise HTTPException(status_code=422, detail="Wrong sorting parameters")
    if page <= 0 or limit <= 0:
        raise HTTPException(status_code=422, detail="Wrong pagination parameters")
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
        escaped_genre = re.sub(r"(\(|\))", r"\\\1", genre)
        query["genre"] = {"$regex": escaped_genre, "$options": "i"}

    books = (
        await books_collection.find(query)
        .sort({sort_by: order})
        .skip(skip)
        .limit(limit)
        .to_list(length=None)
    )
    return books


@router.post("")
async def add_book(_: user_dependency, create_book_model: CreateBookModel):
    book = await books_collection.find_one({"isbn": create_book_model.isbn})
    if book is not None:
        raise HTTPException(
            status_code=409,
            detail=f"Book with ISBN: '{create_book_model.isbn}' already exist",
        )
    if type(create_book_model.img_src) is str:
        create_book_model.img_src = [create_book_model.img_src]

    new_book = BookModel(
        title=[create_book_model.title],
        author=create_book_model.author,
        pages=[] if create_book_model.pages is None else [create_book_model.pages],
        isbn=create_book_model.isbn,
        publisher=(
            []
            if create_book_model.publisher in [None, ""]
            else [create_book_model.publisher]
        ),
        original_title=(
            []
            if create_book_model.original_title in [None, ""]
            else [create_book_model.original_title]
        ),
        release_date=(
            []
            if create_book_model.release_date is None
            else [create_book_model.release_date]
        ),
        release_year=(
            []
            if create_book_model.release_year is None
            else [create_book_model.release_year]
        ),
        polish_release_date=(
            []
            if create_book_model.polish_release_date is None
            else [create_book_model.polish_release_date]
        ),
        img_src=create_book_model.img_src,
        description=(
            ""
            if create_book_model.description is None
            else create_book_model.description
        ),
        genre=create_book_model.genre,
        rating_lc=None,
        rating_gr=None,
        rating_tk=None,
        ratings_lc_number=None,
        ratings_gr_number=None,
        ratings_tk_number=None,
        rating=0,
        ratings_number=0,
    )

    result = await books_collection.insert_one(new_book.model_dump(exclude=["id"]))

    if result.inserted_id:
        return JSONResponse(
            status_code=201, content={"message": "Book added successfully"}
        )
    else:
        raise HTTPException(status_code=500, detail="Failed to add book to database")


@router.delete("/{isbn}", response_description="Delete one book")
async def delete_one_book(_: admin_dependency, isbn: str):
    try:
        isbn_obj = Isbn(isbn)
        if not isbn_obj.validate():
            raise ValueError("ISBN is not valid")
    except:
        raise HTTPException(status_code=422, detail="Not a valid ISBN")

    book = await books_collection.find_one({"isbn": isbn})
    if not book:
        raise HTTPException(status_code=404)

    result = await books_collection.delete_one({"isbn": isbn})
    if result.deleted_count == 1:
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404)


@router.put("/{book_id}")
async def update_book(
    _: admin_dependency, book_id: str, updateBookModel: UpdateBookModel
):
    try:
        book_id_obj = ObjectId(book_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid book ID",
        )
    existing_book = await books_collection.find_one({"_id": book_id_obj})
    if existing_book is None:
        raise HTTPException(status_code=404)

    rating = calculateRating(
        updateBookModel.rating_lc,
        updateBookModel.rating_gr,
        updateBookModel.rating_tk,
        updateBookModel.ratings_lc_number,
        updateBookModel.ratings_gr_number,
        updateBookModel.ratings_tk_number,
    )
    ratings_number = ratingNumberSum(
        updateBookModel.ratings_lc_number,
        updateBookModel.ratings_gr_number,
        updateBookModel.ratings_tk_number,
    )

    updated_data = BookModel(
        **updateBookModel.model_dump(),
        rating=rating,
        ratings_number=ratings_number,
    )
    updated_data = updateBookModel.model_dump(exclude_unset=True)
    result = await books_collection.update_one(
        {"_id": book_id_obj}, {"$set": updated_data}
    )
    if result.modified_count == 1:
        return {"message": "Book updated successfully"}
    raise HTTPException(status_code=500, detail="Failed to update book")
