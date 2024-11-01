from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import Optional
from datetime import datetime

class Image(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", index=True)  # Foreign key to the Profile model
    url: str = Field(index=True)  # Image URL, indexed for sorting
    sort_order: int = Field(default=0)  # Index for sorting
    created_at: datetime = Field(default_factory=datetime.now)

    profile: Optional["Profile"] = Relationship(back_populates="images")
