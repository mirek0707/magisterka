from fastapi import APIRouter, HTTPException
from database.db import books_collection
from models.book import BookModel

router = APIRouter(
    prefix='/books',
    tags=['books'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/{isbn}', response_description='Get one book', response_model=BookModel)
async def get_one_book(isbn: str):
    book = await books_collection.find_one({'isbn': isbn})
    return book


@router.get('/{page}/{limit}/{sort_by}/{order}', response_description='Get one book', response_model=list[BookModel])
async def get_books_per_page(page: int, limit: int, sort_by: str = "ratings_number", order: int = -1):
    if sort_by not in vars(BookModel) or order not in [-1, 1]:
        raise HTTPException(
            status_code=400, detail='Wrong sorting parameters')
    if page <= 0 or limit <= 0:
        raise HTTPException(
            status_code=400, detail='Wrong pagination parameters')
    skip = page * limit - limit
    books = await books_collection.find().sort({sort_by: order}).skip(skip).limit(limit).to_list(length=None)
    return books


@router.post('/ftsearch', response_description='Full-text search in description, title, original_title, author', response_model=list[BookModel])
async def full_text_search_book(query: str, num_of_books: int = 30):
    if not query:
        raise HTTPException(
            status_code=400, detail='Query parameter cannot be empty')

    if len(query) < 3:
        raise HTTPException(
            status_code=400, detail='Query parameter must have at least 3 characters')

    projection = {"score": {"$meta": "textScore"}}
    query = f"\"{query}\""
    books = await books_collection.find(
        {"$text": {"$search": query}},
        projection=projection
    ).to_list(length=None)

    books = sorted(books, key=lambda x: x['score'], reverse=True)
    books = books[:num_of_books]

    return books


@router.post('/search', response_description='Search by author, title or original_title', response_model=list[BookModel])
async def search_book(query: str, num_of_books: int = 5):
    if not query:
        raise HTTPException(
            status_code=400, detail='Query parameter cannot be empty')

    books = await books_collection.find({
        "$or":
        [
            {
                "author": {"$regex": query, "$options": "i"}
            },
            {
                "original_title": {"$regex": query, "$options": "i"}
            },
            {
                "title": {"$regex": query, "$options": "i"}
            }
        ]
    }).to_list(length=None)

    books = sorted(books, key=lambda x: x['ratings_lc_number'], reverse=True)
    books = books[:num_of_books]

    return books
