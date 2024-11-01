from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship




class Employment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)

    profiles: List["Profile"] = Relationship(back_populates="employment")
