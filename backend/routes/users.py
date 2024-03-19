from fastapi import APIRouter, HTTPException, Response
from database.db import users_collection
from models.user import UserModel, CreateUserModel

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={
        201: {"description": "Record created"},
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
        return Response(status_code=201, content="User registered successfully")
    else:
        raise HTTPException(
            status_code=500, detail="Failed to register user to database"
        )
