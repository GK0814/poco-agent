from typing import Any

from pydantic import BaseModel, Field


class MemoryMessage(BaseModel):
    """Memory message payload."""

    role: str = Field(..., description="Role of the message.")
    content: str = Field(..., description="Message content.")


class MemoryCreateRequest(BaseModel):
    """Request to create memories in session scope."""

    session_id: str = Field(..., description="Session identifier.")
    messages: list[MemoryMessage] = Field(
        ...,
        min_length=1,
        description="Conversation messages used to extract and store memories.",
    )
    metadata: dict[str, Any] | None = None


class MemorySearchRequest(BaseModel):
    """Request to search memories in session scope."""

    session_id: str = Field(..., description="Session identifier.")
    query: str = Field(..., description="Search query.")
    filters: dict[str, Any] | None = None


class MemoryUpdateRequest(BaseModel):
    """Request to update memory in session scope."""

    session_id: str = Field(..., description="Session identifier.")
    data: dict[str, Any] = Field(..., description="Updated memory content.")
