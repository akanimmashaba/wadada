from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime, timedelta
from uuid import UUID
from enum import Enum

class SubscriptionStatus(str, Enum):
    ACTIVE = "Active"
    EXPIRED = "Expired"
    CANCELED = "Canceled"

class Discount(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    percentage: float = Field(..., ge=0, le=100)  # Percentage discount (0% to 100%)
    description: Optional[str] = Field(default=None, max_length=500)  # Optional description of the discount
    start_date: Optional[datetime] = Field(default=None)  # When the discount starts
    end_date: Optional[datetime] = Field(default=None)  # When the discount ends
    created_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the subscription was created
    updated_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the subscription was created

    # Back-reference to PlanType
    plans: List["PlanType"] = Relationship(back_populates="discount")

class PlanType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str = Field(unique=True, index=True)  # Plan name, e.g., Free, Premium, VIP
    price: float = Field(default=0.0)  # Price of the plan in dollars
    duration: timedelta  # Duration of the plan, e.g., 30 days, 90 days
    created_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the subscription was created
    updated_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the subscription was created
    def __repr__(self):
        return f"<PlanType(type='{self.type}', price={self.price}, duration={self.duration.days} days)>"
    

# Transaction Model
class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)
    plan_type_id: int = Field(foreign_key="plantype.id")  # Foreign key to PlanType
    transaction_date: datetime
    amount: float
    success: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the subscription was created

    # Relationship to PlanType
    plan_type: Optional[PlanType] = Relationship()

# Subscription Model
class Subscription(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: UUID = Field(foreign_key="profile.supabase_uid", index=True)
    transaction_id: int = Field(foreign_key="transaction.id", index=True)  # Foreign key to Transaction
    start_date: datetime
    end_date: Optional[datetime] = None
    status: SubscriptionStatus = Field(default=SubscriptionStatus.ACTIVE)
    created_at: datetime = Field(default_factory=datetime.now)  # Timestamp for when the subscription was created

    # Relationship to Transaction
    transaction: Optional[Transaction] = Relationship()