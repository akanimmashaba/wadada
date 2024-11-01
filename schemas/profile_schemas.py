# schemas/user_schemas.py
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import date


class CreateProfile(BaseModel):
    name: str
    dob: date
    bio: str

class ViewProfile(BaseModel):
    id: int
    supabase_uid: UUID
    name: str
    dob: date
    bio: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserRegister(BaseModel):
    email: str
    password: str