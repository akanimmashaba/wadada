from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Gender(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)

    # # Relationship back to Profile
    profiles: List["Profile"] = Relationship(back_populates="gender")

    """
    - list genders

    """
