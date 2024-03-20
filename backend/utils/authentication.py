import pytz
import os
from jose import jwt, jwtError
from typing import Annotated
from datetime import timedelta, datetime
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from bson.objectid import ObjectId

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="user/login")


def create_access_token(username: str, id: str, role: str, expires_delta: timedelta):
    encode = {"sub": username, "id": id, "role": role}
    current_date = datetime.now(pytz.timezone("Europe/Warsaw"))
    expires = current_date + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(
        encode, os.environ["SECRET_KEY"], algorithm=os.environ["ALGORITHM"]
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    # role: https://blog.stackademic.com/fastapi-role-base-access-control-with-jwt-9fa2922a088c
    try:
        payload = jwt.decode(
            token, os.environ["SECRET_KEY"], algorithm=os.environ["ALGORITHM"]
        )
        username: str = payload.get("sub")
        id: ObjectId = ObjectId(payload.get("id"))
        role: str = payload.get("role")
        if username is None or id is None or role is None:
            raise HTTPException(
                status_code=401,
                detail="Could not validate user",
            )
        return {"username": username, "id": id, "role": role}
    except jwtError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate user",
        )
