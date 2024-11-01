from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import Optional, List
from datetime import date, datetime

# Import profile-related models
from models.profile_models.children import Children
from models.profile_models.drinking import Drinking
from models.profile_models.education import Education
from models.profile_models.gender import Gender
from models.profile_models.interests import Interest
from models.profile_models.language import Languages
from models.profile_models.location import Location
from models.profile_models.personality import Personality
from models.profile_models.pets import Pets
from models.profile_models.relationship_status import RelationshipStatus
from models.profile_models.religion import Religion
from models.profile_models.seeking import Seeking
from models.profile_models.sexuality import Sexuality
from models.profile_models.smoking import Smoking
from models.profile_models.employment import Employment
from models.profile_models.image import Image
from models.swipe import Swipe
from models.report import Report
from models.notification import Notification
from models.chatroom import ChatRoom
from models.message import Message
from models.block import Block
from models.match import Match
from models.subscription import Subscription, Transaction

class Profile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    supabase_uid: UUID = Field(unique=True, index=True)
    name: str
    dob: date
    bio: Optional[str] = Field(default=None, max_length=500)
    height: Optional[float] = None

    # Foreign Keys
    gender_id: Optional[int] = Field(foreign_key="gender.id", index=True)
    children_id: Optional[int] = Field(default=None, foreign_key="children.id")
    drinking_id: Optional[int] = Field(default=None, foreign_key="drinking.id")
    education_id: Optional[int] = Field(default=None, foreign_key="education.id")
    location_id: Optional[int] = Field(default=None, foreign_key="location.id")
    personality_id: Optional[int] = Field(default=None, foreign_key="personality.id")
    pets_id: Optional[int] = Field(default=None, foreign_key="pets.id")
    relationship_status_id: Optional[int] = Field(default=None, foreign_key="relationshipstatus.id")
    religion_id: Optional[int] = Field(default=None, foreign_key="religion.id")
    seeking_id: Optional[int] = Field(default=None, foreign_key="seeking.id")
    sexuality_id: Optional[int] = Field(default=None, foreign_key="sexuality.id")
    smoking_id: Optional[int] = Field(default=None, foreign_key="smoking.id")
    employment_id: Optional[int] = Field(default=None, foreign_key="employment.id")

    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=False)

    # Relationships
    images: List[Image] = Relationship(back_populates="profile")

    gender: Optional[Gender] = Relationship(back_populates="profiles")
    children: Optional[Children] = Relationship(back_populates="profiles")
    drinking: Optional[Drinking] = Relationship(back_populates="profiles")
    educations: Optional[Education] = Relationship(back_populates="profiles")
    location: Optional[Location] = Relationship(back_populates="profiles")
    personality: Optional[Personality] = Relationship(back_populates="profiles")
    pets: Optional[Pets] = Relationship(back_populates="profiles")
    relationship_status: Optional[RelationshipStatus] = Relationship(back_populates="profiles")
    religion: Optional[Religion] = Relationship(back_populates="profiles")
    seeking: Optional[Seeking] = Relationship(back_populates="profiles")
    sexuality: Optional[Sexuality] = Relationship(back_populates="profiles")
    smoking: Optional[Smoking] = Relationship(back_populates="profiles")
    employment: Optional[Employment] = Relationship(back_populates="profiles")
    interests: List[Interest] = Relationship(back_populates="profiles")
    languages: List[Languages] = Relationship(back_populates="profiles")
    notifications: List[Notification] = Relationship(back_populates="user")
    chat_rooms: List[ChatRoom] = Relationship(back_populates="users")
    messages: List[Message] = Relationship(back_populates="sender")
    blocked_users: List[Block] = Relationship(back_populates="blocker")
    blocking_users: List[Block] = Relationship(back_populates="blocked")
    matches_as_user_one: List[Match] = Relationship(back_populates="user_one")
    matches_as_user_two: List[Match] = Relationship(back_populates="user_two")

    subscriptions: List["Subscription"] = Relationship(back_populates="profile")
    transactions: List["Transaction"] = Relationship(back_populates="profile")

    # Swipe relationships
    outgoing_swipes: List[Swipe] = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Swipe.swiper_id == Profile.supabase_uid"}
    )
    incoming_swipes: List[Swipe] = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Swipe.swiped_id == Profile.supabase_uid"}
    )

    # Report relationships
    outgoing_reports: List[Report] = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Report.reporter_id == Profile.supabase_uid"}
    )
    incoming_reports: List[Report] = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Report.reported_id == Profile.supabase_uid"}
    )
