from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from typing import Optional, List
from datetime import datetime

# Import any models that are needed for foreign keys or relationships
from models.profile_models.gender import Gender
from models.profile_models.relationship_status import RelationshipStatus
from models.profile_models.religion import Religion
from models.profile_models.education import Education
from models.profile_models.smoking import Smoking
from models.profile_models.drinking import Drinking
from models.profile_models.pets import Pets

class UserPreference(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", index=True)  # Foreign key to the Profile model
    
    # Preferred age range
    min_age: Optional[int] = Field(default=18)  # Minimum age preference
    max_age: Optional[int] = Field(default=99)  # Maximum age preference

    # Preferred distance for potential matches in kilometers/miles
    max_distance: Optional[int] = Field(default=50)  

    # Preferred gender
    # gender_id: Optional[int] = Field(foreign_key="gender.id", index=True) 

    # Preferred relationship status
    relationship_status_id: Optional[int] = Field(foreign_key="relationshipstatus.id", index=True)

    # Preferences for religion, education, smoking, drinking, and pets
    religion_id: Optional[int] = Field(foreign_key="religion.id", index=True)
    education_id: Optional[int] = Field(foreign_key="education.id", index=True)
    smoking_id: Optional[int] = Field(foreign_key="smoking.id", index=True)
    drinking_id: Optional[int] = Field(foreign_key="drinking.id", index=True)
    pets_id: Optional[int] = Field(foreign_key="pets.id", index=True)

    # Timestamps for tracking creation and updates
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=False)

    # Relationships to the referenced models
    gender: Optional[Gender] = Relationship()
    relationship_status: Optional[RelationshipStatus] = Relationship()
    religion: Optional[Religion] = Relationship()
    education: Optional[Education] = Relationship()
    smoking: Optional[Smoking] = Relationship()
    drinking: Optional[Drinking] = Relationship()
    pets: Optional[Pets] = Relationship()
