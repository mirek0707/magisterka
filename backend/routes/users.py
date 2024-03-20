from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from database.db import users_collection
from models.user import UserModel, CreateUserModel, bcrypt_context
from models.token import Token
from fastapi.security import OAuth2PasswordRequestForm
from utils.authentication import create_access_token


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={
        201: {"description": "Record created"},
        400: {"description": "Bad request"},
        404: {"description": "Not found"},
        409: {"description": "Conflict, record already in database"},
        500: {"description": "Internal server error"},
    },
)


@router.post("/register", response_description="Register a new user")
async def create_user(create_user_model: CreateUserModel):
    print(create_user_model)
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
    else:
        raise HTTPException(
            status_code=500, detail="Failed to register user to database"
        )


@router.post(
    "/login",
    response_description="Login to your account and get access token",
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
