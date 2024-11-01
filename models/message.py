from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import List, Optional
from datetime import datetime
from models.chatroom import ChatRoom


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary key for the message
    chat_room_id: int = Field(foreign_key="chatroom.id", index=True)  # Foreign key to the ChatRoom model
    sender_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # The user who sent the message
    content: str  # The content of the message
    created_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the message was sent

    # Relationships
    chat_room: "ChatRoom" = Relationship(back_populates="messages")  # Relationship to the ChatRoom
    sender: Optional["Profile"] = Relationship()  # Relationship to the Profile who sent the message
