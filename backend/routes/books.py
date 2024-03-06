from fastapi import APIRouter
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
    print(type(book))
    return book
