from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from datetime import datetime


class Personality(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    profiles: List["Profile"] = Relationship(back_populates="personality")

    """
    list personalities
    """
