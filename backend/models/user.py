from pydantic import ConfigDict, BaseModel, Field, EmailStr
from typing import Optional
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
from models.userRole import UserRole

PyObjectId = Annotated[str, BeforeValidator(str)]


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
