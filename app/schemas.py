from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime


class OpeningProviderSchemas(BaseModel):
    name: str
    domain: str
    description: str


class UserRegistrationSchemas(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class LoginSchemas(BaseModel):
    email: str
    password: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str
