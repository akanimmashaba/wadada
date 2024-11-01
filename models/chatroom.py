from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import List
from datetime import datetime
from typing import Optional

class ChatRoom(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary key for the chat room
    name: str  # Name of the chat room
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.UTC))  # Timestamp for when the chat room was created
    updated_at: datetime = Field(default_factory=lambda: datetime.now(datetime.UTC))  # Timestamp for when the chat room was last updated
    is_encrypted: bool = Field(default=True)  # Indicates if the chat is encrypted

    # Relationships
    users: List["Profile"] = Relationship(back_populates="chat_rooms")  # Users in the chat room
    messages: List["Message"] = Relationship(back_populates="chat_room")  # Messages in the chat room
