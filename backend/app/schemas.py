from typing import Literal
from pydantic import BaseModel, Field

class Barrier(BaseModel):
    label: str
    visible_evidence: str
    affected_users: list[str]
    urgency: Literal["low", "medium", "high"]
    confidence: float = Field(ge=0, le=1)
    box_2d: list[int] | None = Field(default=None, min_length=4, max_length=4)
    immediate_guidance: str
    low_cost_action: str
    structural_action: str

class AuditResult(BaseModel):
    summary: str
    status: Literal["likely_accessible", "needs_review", "potential_barrier", "no_barrier_visible", "insufficient_evidence", "immediate_safety_concern"]
    overall_confidence: float = Field(ge=0, le=1)
    barriers: list[Barrier] = Field(default_factory=list, max_length=3)
    cannot_confirm: list[str] = Field(default_factory=list)
    visitor_guidance: str
    manager_actions: list[str] = Field(default_factory=list)
    report_text: str
    evidence_quality: Literal["low", "medium", "high"] = "medium"
    requested_photos: list[str] = Field(default_factory=list, max_length=4)
    requires_review: bool = False
    consistency_warning: str | None = None
