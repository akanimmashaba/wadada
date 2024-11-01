from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Pets(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    profiles: List["Profile"] = Relationship(back_populates="pets")

    """
    - i'd like them some day
    - i'd like them soon
    - i dont want kids
    - i already have kids
    - i have one child
    - i'd rather not say
    - pet free
    - like but dont have 
    - rather not say
    """