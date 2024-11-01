from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import Optional
from datetime import datetime

class Block(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary key for the block
    blocker_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # User who is blocking another user
    blocked_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # User who is being blocked
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.UTC))  # Timestamp for when the chat room was created
    
    # Relationships
    blocker: Optional["Profile"] = Relationship(back_populates="blocked_users")  # Relationship to the Profile of the blocker
    blocked: Optional["Profile"] = Relationship(back_populates="blocking_users")  # Relationship to the Profile of the blocked user
