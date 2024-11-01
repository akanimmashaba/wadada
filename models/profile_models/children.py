from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Children(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    
    profiles: List["Profile"] = Relationship(back_populates="children")

    """
    - i'd like them some day
    - i'd like them soon
    - i dont want kids
    - i already have kids
    - i have one child
    - i'd rather not say
    """ 