from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import Optional
from datetime import datetime

class Report(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    reporter_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # User who is making the report
    reported_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)  # User who is being reported
    reason: str = Field(max_length=100)  # Reason for the report, e.g., "Spam", "Harassment"
    description: Optional[str] = Field(default=None, max_length=1000)  # Optional detailed description
    created_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the report was created
    reviewed: bool = Field(default=False)  # Whether the report has been reviewed by an admin
    action_taken: Optional[str] = Field(default=None, max_length=100)  # Action taken after review (e.g., "User Banned")

    # Relationships
    reporter: Optional["Profile"] = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Report.reporter_id == Profile.supabase_uid"},
        back_populates="outgoing_reports"
    )
    reported: Optional["Profile"] = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Report.reported_id == Profile.supabase_uid"},
        back_populates="incoming_reports"
    )
