from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


# Persistent models (stored in database for local caching/backup)
class UserSubmission(SQLModel, table=True):
    """User submission data stored locally and synced to Airtable."""

    __tablename__ = "user_submissions"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    email: str = Field(max_length=255, regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    business_details: str = Field(max_length=5000)
    airtable_record_id: Optional[str] = Field(default=None, max_length=100)
    synced_to_airtable: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Non-persistent schemas (for validation, forms, API requests/responses)
class UserSubmissionCreate(SQLModel, table=False):
    """Schema for creating new user submissions."""

    name: str = Field(max_length=100)
    email: str = Field(max_length=255, regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    business_details: str = Field(max_length=5000)


class UserSubmissionUpdate(SQLModel, table=False):
    """Schema for updating existing user submissions."""

    name: Optional[str] = Field(default=None, max_length=100)
    email: Optional[str] = Field(
        default=None, max_length=255, regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )
    business_details: Optional[str] = Field(default=None, max_length=5000)
    airtable_record_id: Optional[str] = Field(default=None, max_length=100)
    synced_to_airtable: Optional[bool] = Field(default=None)


class AirtableConfig(SQLModel, table=False):
    """Configuration schema for Airtable integration."""

    base_id: str = Field(max_length=100)
    table_name: str = Field(max_length=100)
    api_key: str = Field(max_length=200)


class UserSubmissionResponse(SQLModel, table=False):
    """Schema for user submission API responses."""

    id: int
    name: str
    email: str
    business_details: str
    airtable_record_id: Optional[str]
    synced_to_airtable: bool
    created_at: str  # ISO format datetime string
    updated_at: str  # ISO format datetime string
