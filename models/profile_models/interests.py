from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Interest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True)
    profiles: List["Profile"] = Relationship(back_populates="interests")


