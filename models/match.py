from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import Optional
from datetime import datetime

class Match(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary key for the match
    user_one_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # ID of the first user in the match
    user_two_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # ID of the second user in the match
    created_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the match was created

    # Relationships
    user_one: Optional["Profile"] = Relationship(back_populates="matches_as_user_one")  # Relationship to the first user
    user_two: Optional["Profile"] = Relationship(back_populates="matches_as_user_two")  # Relationship to the second user
