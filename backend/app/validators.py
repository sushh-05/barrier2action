from app.schemas import AuditResult

CONCERN_WORDS = ("steps", "stairs", "blocked", "obstruction", "uneven", "curb", "no ramp", "barrier", "trip hazard", "slippery")

def validate_audit_consistency(result: AuditResult) -> AuditResult:
    narrative = " ".join((result.summary, result.visitor_guidance)).lower()
    if any(word in narrative for word in CONCERN_WORDS) and not result.barriers:
        result.status = "insufficient_evidence"
        result.requires_review = True
        result.consistency_warning = "A possible accessibility concern was mentioned but was not returned as structured evidence. Capture a closer view before treating this as clear or accessible."
        if not result.requested_photos:
            result.requested_photos = ["Take a closer, level photo of the suspected steps, curb, or obstruction.", "Photograph the full entrance and threshold from 2–3 metres away."]
    return result
