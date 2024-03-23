from pydantic import ConfigDict, BaseModel, Field, EmailStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
from models.userRole import UserRole
from passlib.context import CryptContext

PyObjectId = Annotated[str, BeforeValidator(str)]

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserModel(BaseModel):
    """
    Container for a single user record.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str = Field(...)
    password: str = Field(...)
    email: EmailStr = Field(...)
    role: UserRole

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "_id": "65e5e5f41d43dc0277b22066",
                "username": "Mirek_0707",
                "password": "41d43dc0277b2206",
                "email": "mirek0707@interia.pl",
                "role": "USER",
            }
        },
    )


class CreateUserModel(BaseModel):
    """
    Container for a create user request.
    """

    username: str = Field(...)
    password: str = Field(...)
    email: EmailStr = Field(...)
    role: UserRole

    @field_validator("password")
    def validate_password(cls, password: str):
        if len(password) < 6:
            raise ValueError(f"Password is too short")
        return bcrypt_context.hash(password)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "username": "Mirek_0707",
                "password": "41d43dc0277b2206",
                "email": "mirek0707@interia.pl",
                "role": "USER",
            }
        },
    )


class GetUserModel(BaseModel):
    """
    Container for a single user data without password.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str = Field(...)
    email: EmailStr = Field(...)
    role: UserRole

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "_id": "65e5e5f41d43dc0277b22066",
                "username": "Mirek_0707",
                "email": "mirek0707@interia.pl",
                "role": "USER",
            }
        },
    )
