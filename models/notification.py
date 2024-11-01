from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import Optional
from datetime import datetime

class Notification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary key for the notification
    user_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # The user who will receive the notification
    type: str  # Type of notification (e.g., "like", "message", "match")
    content: str  # Content of the notification
    is_read: bool = Field(default=False)  # Flag to indicate if the notification has been read
    created_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the notification was created

    # Relationship to the Profile model
    user: Optional["Profile"] = Relationship(back_populates="notifications")
