from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import Optional, List
from datetime import datetime

class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # user_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # Foreign key to the Profile model
    latitude: float = None
    longitude: float = None   
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.UTC))  # Timestamp for when the chat room was created
    
    profiles: List["Profile"] = Relationship(back_populates="location")  # Back relationship to Profile
