from models.userRole import UserRole
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from database.db import shelves_collection
from models.shelf import ShelfModel
from utils.authentication import (
    admin_dependency,
    user_dependency,
    current_user_depedency,
)
from bson.objectid import ObjectId, InvalidId
from pyisbn import Isbn

router = APIRouter(
    prefix="/shelf",
    tags=["shelf"],
    responses={
        400: {"description": "Bad request"},
        404: {"description": "Not found"},
        409: {"description": "Conflict"},
    },
)


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
        result = await shelves_collection.delete_one({"_id": shelf_id_object})
        if result.deleted_count == 1:
            return JSONResponse(
                status_code=200, content={"message": "Shelf deleted successfully"}
            )
        raise HTTPException(status_code=404, detail="Shelf not found")
    raise HTTPException(
        status_code=401,
        detail="You don't have enough permissions",
    )
