from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from database.db import users_collection
from models.user import (
    UserModel,
    CreateUserModel,
    GetUserModel,
    bcrypt_context,
    EditUserModel,
)
from models.userRole import UserRole
from models.token import Token
from fastapi.security import OAuth2PasswordRequestForm
from utils.authentication import (
    create_access_token,
    user_dependency,
    current_user_depedency,
)
from bson.objectid import ObjectId, InvalidId


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={
        200: {"description": "OK"},
        201: {"description": "Record created"},
        400: {"description": "Bad request"},
        401: {"description": "Unauthorized"},
        404: {"description": "Not found"},
        409: {"description": "Conflict, record already in database"},
        500: {"description": "Internal server error"},
    },
)


@router.post("/register", response_description="Create a new user")
async def create_user(create_user_model: CreateUserModel):
    existing_username = await users_collection.find_one(
        {"username": create_user_model.username}
    )
    existing_email = await users_collection.find_one({"email": create_user_model.email})
    if existing_username or existing_email:
        raise HTTPException(
            status_code=409, detail="Username or email already registered"
        )
    new_user = UserModel(**create_user_model.model_dump())

    result = await users_collection.insert_one(new_user.model_dump(exclude=["id"]))

    if result.inserted_id:
        return JSONResponse(
            status_code=201, content={"message": "User registered successfully"}
        )

    raise HTTPException(status_code=500, detail="Failed to register user to database")


@router.post(
    "/login",
    response_description="Get users access token",
    response_model=Token,
)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await users_collection.find_one({"username": form_data.username})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not bcrypt_context.verify(form_data.password, user["password"]):
        raise HTTPException(
            status_code=400,
            detail="Incorrect password",
        )

    token = create_access_token(
        user["username"], str(user["_id"]), user["role"], timedelta(hours=4)
    )

    return {"access_token": token, "token_type": "Bearer"}


@router.get(
    "/{user_id}", response_description="Get user data", response_model=GetUserModel
)
async def get_user_info(_: user_dependency, user_id: str):
    try:
        user_id_object = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid user ID",
        )
    user = await users_collection.find_one({"_id": user_id_object})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return GetUserModel.model_validate(user)


@router.put("/edit", response_description="Edit a user")
async def edit_user(
    _: user_dependency, curr_user: current_user_depedency, edit_user: EditUserModel
):
    user_id_object = ObjectId(edit_user.id)
    if (
        UserRole(curr_user["role"]) is UserRole.ADMIN
        or curr_user["id"] == user_id_object
    ):
        result = await users_collection.update_one(
            {"_id": user_id_object}, {"$set": edit_user.model_dump(exclude=["id"])}
        )
        if result.modified_count == 1:
            return {"message": "User updated successfully"}
        elif result.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        elif result.modified_count == 0:
            raise HTTPException(
                status_code=409,
                detail="User data does not change in query",
            )
        raise HTTPException(status_code=500, detail="Failed to edit user")
    raise HTTPException(
        status_code=401,
        detail="You don't have enough permissions",
    )


@router.delete("/{user_id}", response_description="Delete user account")
async def delete_user_account(
    _: user_dependency, curr_user: current_user_depedency, user_id: str
):
    try:
        user_id_object = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid user ID",
        )
    if (
        UserRole(curr_user["role"]) is UserRole.ADMIN
        or curr_user["id"] == user_id_object
    ):
        result = await users_collection.delete_one({"_id": user_id_object})
        if result.deleted_count == 1:
            return {"message": "User deleted successfully"}
        raise HTTPException(status_code=404, detail="User not found")
    raise HTTPException(
        status_code=401,
        detail="You don't have enough permissions",
    )
