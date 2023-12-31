from pydantic import BaseModel, EmailStr, Field


class BaseValidator(BaseModel):
    pass


class Users(BaseModel):
    username: str
    password: str
    company_name: str
    address: str
    phone_number: str
    email: EmailStr


class UserLogin(BaseValidator):
    password: str = Field(
        ...,
        alias="password",
        name="password",
        isRquired=True,

    )
    username: str = Field(
        ...,
        alias="username",
        name="username",
        dataType="text",
        regexPatternPattern=r"^[a-zA-Z0-9_]{3,32}$",
        isRquired=True,
    )


class ConfirmUser(BaseModel):
    username: str = Field(
        ...,
        alias="username",
        name="username",
        isRquired=True,

    )
    status: bool = Field(
        ...,
        alias="status",
        name="status",
        isRquired=True,
    )
