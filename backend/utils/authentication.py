import pytz
import os
from jose import jwt, JWTError
from typing import Annotated
from datetime import timedelta, datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from bson.objectid import ObjectId
from models.userRole import UserRole

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/user/login")


def create_access_token(
    username: str, email: str, id: str, role: str, expires_delta: timedelta
):
    encode = {"sub": username, "email": email, "id": id, "role": role}
    current_date = datetime.now(pytz.timezone("Europe/Warsaw"))
    expires = current_date + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(
        encode, os.environ["SECRET_KEY"], algorithm=os.environ["ALGORITHM"]
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate user",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, os.environ["SECRET_KEY"], algorithms=[os.environ["ALGORITHM"]]
        )
        username: str = payload.get("sub")
        email: str = payload.get("email")
        id: ObjectId = ObjectId(payload.get("id"))
        role: str = payload.get("role")

        if username is None or id is None or role is None or email is None:
            raise credentials_exception
        return {"username": username, "email": email, "id": id, "role": role}
    except JWTError:
        raise credentials_exception


current_user_depedency = Annotated[dict, Depends(get_current_user)]


class RoleChecker:
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def __call__(self, user: current_user_depedency):
        if user["role"] in self.allowed_roles:
            return True
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You don't have enough permissions",
        )


admin_dependency = Annotated[bool, Depends(RoleChecker(allowed_roles=[UserRole.ADMIN]))]
user_dependency = Annotated[
    bool, Depends(RoleChecker(allowed_roles=[UserRole.USER, UserRole.ADMIN]))
]
