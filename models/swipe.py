from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from datetime import datetime
from typing import Optional

class Swipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    swiper_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # The user who swiped
    swiped_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # The user who was swiped on
    is_like: bool  # True for a right swipe (like), False for a left swipe (dislike)
    created_at: datetime = Field(default_factory=datetime.now)

    # Relationships
    swiper: Optional["Profile"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Swipe.swiper_id]"})
    swiped: Optional["Profile"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Swipe.swiped_id]"})
    
