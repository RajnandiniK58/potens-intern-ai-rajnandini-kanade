from typing import Optional

from pydantic import BaseModel


class TriageRequest(BaseModel):
    """Input payload for telecom ticket triage requests."""

    customer_id: str
    message: str
    location: Optional[str] = None


class TriageResponse(BaseModel):
    """Structured output returned after triaging a support ticket."""

    category: str
    priority: str
    next_tool: str
    reasoning: str
    why: str
