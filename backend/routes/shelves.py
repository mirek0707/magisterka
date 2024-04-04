from models.userRole import UserRole
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from database.db import shelves_collection, books_collection
from models.shelf import ShelfModel
from models.book import BookModel
from pydantic import HttpUrl
from utils.authentication import (
    user_dependency,
    current_user_depedency,
)
from utils.spider import get_shelves, get_userId, get_books_from_shelf, get_book_content
from utils.other import merge_values
from utils.rating import calculateRating, ratingNumberSum
from bson.objectid import ObjectId, InvalidId
from pyisbn import Isbn
import requests

router = APIRouter(
    prefix="/shelf",
    tags=["shelf"],
    responses={
        200: {"description": "OK"},
        201: {"description": "Shelf created"},
        400: {"description": "Bad request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not found"},
        409: {"description": "Conflict"},
        422: {"description": "Unprocessable content"},
        500: {"description": "Internal server error"},
    },
)


@router.put(
    "/importLC",
    response_description="import shelves with books from lubimyczytac",
)
async def run_lc_shelves_spider(
    url: str, curr_user: current_user_depedency, _: user_dependency
):
    try:
        HttpUrl(url)
    except:
        raise HTTPException(status_code=400)
    shelves = get_shelves(url)
    uid = get_userId(url)

    shelves_with_books = dict()
    request_url = "https://lubimyczytac.pl/profile/getLibraryBooksList"
    for k, v in shelves.items():
        print(v)
        page = 1
        shelf_links = list()
        while True:
            try:
                response = requests.post(
                    request_url,
                    data={
                        "page": page,
                        "listId": "booksFilteredList",
                        "kolejnosc": "data-dodania",
                        "showFirstLetter": "0",
                        "listType": "list",
                        "objectId": uid,
                        "own": "0",
                        "shelfs[]": v,
                        "paginatorType": "Standard",
                    },
                    headers={
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "X-Requested-With": "XMLHttpRequest",
                        "Host": "lubimyczytac.pl",
                    },
                )
                response.raise_for_status()
                links = get_books_from_shelf(response.json()["data"]["content"])
                shelf_links.extend(links)
                page += 1

            except requests.exceptions.RequestException as e:
                print("nie dziala cos", e)
                break

        shelves_with_books[k] = shelf_links

    books_set = list()
    for k, v in shelves_with_books.items():
        for i in range(len(v)):
            book = get_book_content(shelves_with_books[k][i])
            if book is not None:
                shelves_with_books[k][i] = book["isbn"]
                books_set.append(book)

    for k, v in shelves_with_books.items():
        shelves_with_books[k] = [item for item in v if "http" not in item]

    list({v["isbn"]: v for v in books_set}.values())

    for k, v in shelves_with_books.items():
        shelf = await shelves_collection.find_one(
            {"user_id": ObjectId(curr_user["id"]), "name": k}
        )
        if not shelf:
            result = await shelves_collection.insert_one(
                {
                    "name": k,
                    "user_id": ObjectId(curr_user["id"]),
                    "books": v,
                    "is_default": False,
                }
            )

            if result.inserted_id:
                print(f"Shelf '{k}' added successfully")
            else:
                print(f"Failed to add shelf '{k}'")
        else:
            result = await shelves_collection.update_one(
                {"_id": shelf["_id"]}, {"$addToSet": {"books": {"$each": v}}}
            )
            if result.modified_count == 1:
                print(f"Shelf '{k}' updated successfully")
            elif result.modified_count == 0:
                print(f"Books already exists on the shelf '{k}'")
            else:
                print(f"Shelf '{k}' update failed")

    print("\n")
    for book in books_set:
        isbn = book["isbn"]
        existing_book = await books_collection.find_one({"isbn": isbn})
        if not existing_book:
            new_book = BookModel(
                id=None,
                isbn=isbn,
                title=book["title"],
                author=book["author"],
                pages=book["pages"],
                publisher=book["publisher"],
                original_title=book["original_title"],
                release_date=book["release_date"],
                release_year=None,
                polish_release_date=book["polish_release_date"],
                rating_lc=book["rating_lc"],
                ratings_lc_number=book["ratings_lc_number"],
                rating_gr=None,
                rating_tk=None,
                ratings_gr_number=None,
                ratings_tk_number=None,
                rating=book["rating_lc"] / 2,
                ratings_number=book["ratings_lc_number"],
                genre=book["genre"],
                description=book["description"],
                img_src=book["img_src"],
            )
            result = await books_collection.insert_one(
                new_book.model_dump(exclude=["id"])
            )
            if result.inserted_id:
                print(f"Book '{isbn}' added successfully")
            else:
                print(f"Failed to add book '{isbn}'")
        else:
            update = BookModel(
                id=None,
                isbn=isbn,
                title=merge_values(existing_book["title"], book["title"]),
                author=merge_values(existing_book["author"], book["author"]),
                pages=merge_values(existing_book["pages"], book["pages"]),
                publisher=merge_values(existing_book["publisher"], book["publisher"]),
                original_title=merge_values(
                    existing_book["original_title"], book["original_title"]
                ),
                release_date=merge_values(
                    existing_book["release_date"], book["release_date"]
                ),
                release_year=existing_book["release_year"],
                polish_release_date=merge_values(
                    existing_book["polish_release_date"], book["polish_release_date"]
                ),
                rating_lc=book["rating_lc"],
                ratings_lc_number=book["ratings_lc_number"],
                rating_gr=existing_book["rating_gr"],
                rating_tk=existing_book["rating_tk"],
                ratings_gr_number=existing_book["ratings_gr_number"],
                ratings_tk_number=existing_book["ratings_tk_number"],
                rating=calculateRating(
                    book["rating_lc"],
                    existing_book["rating_gr"],
                    existing_book["rating_tk"],
                    book["ratings_lc_number"],
                    existing_book["ratings_gr_number"],
                    existing_book["ratings_tk_number"],
                ),
                ratings_number=ratingNumberSum(
                    book["ratings_lc_number"],
                    existing_book["ratings_gr_number"],
                    existing_book["ratings_tk_number"],
                ),
                genre=book["genre"],
                description=book["description"],
                img_src=merge_values(
                    existing_book["img_src"],
                    book["img_src"],
                ),
            )
            result = await books_collection.update_one(
                {"isbn": isbn}, {"$set": update.model_dump(exclude=["id", "isbn"])}
            )
            if result.modified_count == 1:
                print(f"Book '{isbn}' updated successfully")
            elif result.modified_count == 0:
                print(f"Book '{isbn}' data does not changed")
            else:
                print(f"Book '{isbn}' update failed")

    return {
        "shelves": shelves,
        "uid": uid,
        "shelves_with_books": shelves_with_books,
        "books": books_set,
    }


@router.get(
    "/{user_id}/{shelf_id}",
    response_description="Get single shelf",
    response_model=ShelfModel,
)
async def get_one_shelf(user_id: str, shelf_id: str, _: user_dependency):
    try:
        user_id_object = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid user ID",
        )
    try:
        shelf_id_object = ObjectId(shelf_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid shelf ID",
        )

    shelf = await shelves_collection.find_one(
        {"_id": shelf_id_object, "user_id": user_id_object}
    )
    if not shelf:
        raise HTTPException(status_code=404)
    return shelf


@router.post(
    "/add",
    response_description="Add shelf",
)
async def add_shelf(name: str, curr_user: current_user_depedency, _: user_dependency):
    shelf = await shelves_collection.find_one(
        {"user_id": ObjectId(curr_user["id"]), "name": name}
    )
    if not shelf:
        result = await shelves_collection.insert_one(
            {
                "name": name,
                "user_id": ObjectId(curr_user["id"]),
                "books": list(),
                "is_default": False,
            }
        )

        if result.inserted_id:
            return JSONResponse(
                status_code=201, content={"message": "Shelf added successfully"}
            )
        else:
            raise HTTPException(status_code=500, detail="Failed to add shelf")
    else:
        raise HTTPException(
            status_code=409,
            detail=f"Shelf with name: '{name}' already exist for current user",
        )


@router.get(
    "/{user_id}",
    response_description="Get all user's shelves",
    response_model=list[ShelfModel],
)
async def get_user_shelves(user_id: str, _: user_dependency):
    try:
        user_id_object = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid user ID",
        )
    shelves = (
        await shelves_collection.find({"user_id": user_id_object})
        .sort({"name": 1})
        .to_list(length=None)
    )
    if not shelves:
        raise HTTPException(status_code=404)
    return shelves


@router.patch(
    "/{shelf_id}/add/{isbn}",
    response_description="Add book to shelf",
)
async def add_book_to_shelf(
    shelf_id: str, isbn: str, curr_user: current_user_depedency, _: user_dependency
):
    try:
        shelf_id_object = ObjectId(shelf_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid shelf ID",
        )
    try:
        isbn_obj = Isbn(isbn)
        if not isbn_obj.validate():
            raise ValueError("ISBN is not valid")
    except:
        raise HTTPException(status_code=422, detail="Not a valid ISBN")

    shelf = await shelves_collection.find_one({"_id": shelf_id_object})
    if (
        UserRole(curr_user["role"]) is UserRole.ADMIN
        or curr_user["id"] == shelf["user_id"]
    ):
        result = await shelves_collection.update_one(
            {"_id": shelf_id_object}, {"$addToSet": {"books": isbn}}
        )
        if result.modified_count == 1:
            return {"message": "Shelf updated successfully"}
        elif result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Shelf not found")
        elif result.modified_count == 0:
            raise HTTPException(
                status_code=409,
                detail="Book already exists on the shelf",
            )
        raise HTTPException(status_code=500, detail="Failed to add book to shelf")
    raise HTTPException(
        status_code=401,
        detail="You don't have enough permissions",
    )


@router.patch(
    "/{shelf_id}/del/{isbn}",
    response_description="Delete book from shelf",
)
async def delete_book_from_shelf(
    shelf_id: str, isbn: str, curr_user: current_user_depedency, _: user_dependency
):
    try:
        shelf_id_object = ObjectId(shelf_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid shelf ID",
        )
    try:
        isbn_obj = Isbn(isbn)
        if not isbn_obj.validate():
            raise ValueError("ISBN is not valid")
    except:
        raise HTTPException(status_code=422, detail="Not a valid ISBN")

    shelf = await shelves_collection.find_one({"_id": shelf_id_object})
    if (
        UserRole(curr_user["role"]) is UserRole.ADMIN
        or curr_user["id"] == shelf["user_id"]
    ):
        result = await shelves_collection.update_one(
            {"_id": shelf_id_object}, {"$pull": {"books": isbn}}
        )
        if result.modified_count == 1:
            return {"message": "Shelf updated successfully"}
        elif result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Shelf not found")
        elif result.modified_count == 0:
            raise HTTPException(
                status_code=409,
                detail="Book not found on the shelf",
            )
        raise HTTPException(status_code=500, detail="Failed to delete book from shelf")
    raise HTTPException(
        status_code=401,
        detail="You don't have enough permissions",
    )


@router.delete("/{shelf_id}", response_description="Delete shelf")
async def delete_shelf(
    _: user_dependency, curr_user: current_user_depedency, shelf_id: str
):
    try:
        shelf_id_object = ObjectId(shelf_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid shelf ID",
        )
    shelf = await shelves_collection.find_one({"_id": shelf_id_object})
    if (
        UserRole(curr_user["role"]) is UserRole.ADMIN
        or curr_user["id"] == shelf["user_id"]
    ):
        if shelf["is_default"]:
            raise HTTPException(
                status_code=403,
                detail="Shelf is marked as default and it can't be deleted",
            )

        result = await shelves_collection.delete_one({"_id": shelf_id_object})
        if result.deleted_count == 1:
            return {"message": "Shelf deleted successfully"}
        raise HTTPException(status_code=404, detail="Shelf not found")
    raise HTTPException(
        status_code=401,
        detail="You don't have enough permissions",
    )
