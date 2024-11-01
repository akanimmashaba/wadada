from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from ..profile import Profile  # Import only for type checking


class Education(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # profile_id: int = Field(foreign_key="profile.id", index=True)  # Foreign key to the Profile model
    institution: Optional[str]
    currently_studying: bool = Field(default=False)  # Whether the user is currently studying here
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.UTC))  # Timestamp for when the chat room was created
    updated_at: datetime = Field(default_factory=lambda: datetime.now(datetime.UTC))  # Timestamp for when the chat room was last updated
    
    # Relationship to the Profile model
    profile: "Profile" = Relationship(back_populates="educations")
