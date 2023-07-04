from fastapi_users import schemas
from pydantic import Field

password_regex = "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})"


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    password: str = Field(..., regex=password_regex)


class UserUpdate(schemas.BaseUserUpdate):
    password: str = Field(..., regex=password_regex)
