from fastapi import APIRouter, HTTPException
from database.db import users_collection
from models.user import UserModel, CreateUserModel

router = APIRouter(
    prefix="/user", tags=["user"], responses={404: {"description": "Not found"}}
)


@router.post(
    "/register", response_description="Register a new user", response_model=UserModel
)
async def create_user(create_user_model: CreateUserModel):
    print(create_user_model)
    existing_username = await users_collection.find_one(
        {"username": create_user_model.username}
    )
    existing_email = await users_collection.find_one({"email": create_user_model.email})
    if existing_username or existing_email:
        raise HTTPException(
            status_code=400, detail="Username or email already registered"
        )
    new_user = UserModel(**create_user_model.model_dump())
    print(new_user)
    return new_user
