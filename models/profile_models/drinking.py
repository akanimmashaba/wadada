from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List



class Drinking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)

    profiles: List["Profile"] = Relationship(back_populates="drinking")

   
    """
    - socially
    - never
    - oftern
    - no, im sober
    - i'd rather not say

    """