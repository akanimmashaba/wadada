from datetime import datetime, date
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
from pydantic import EmailStr, field_validator


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    supabase_uid: str = Field(unique=True, index=True)  # Link to Supabase auth user
    email: EmailStr = Field(unique=True, index=True)
    first_name: str = Field(min_length=2, max_length=50)
    is_active: bool = Field(default=True)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
