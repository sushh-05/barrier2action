from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from app.config import get_settings
from app.gemini_service import GeminiServiceError, analyze_accessibility
from app.image_utils import process_image
from app.schemas import AuditResult
router = APIRouter(prefix="/api", tags=["Audit"])
@router.post("/audit", response_model=AuditResult)
async def create_audit(image: UploadFile = File(...), follow_up_images: list[UploadFile] = File(default=[]), place_type: str = Form(...), perspective: str = Form(...), location_description: str = Form("")):
    if len(location_description) > 300: raise HTTPException(422, "Description must be 300 characters or fewer.")
    try:
        raw = await image.read(); image_bytes, mime_type = process_image(raw, image.content_type or "", get_settings().max_image_mb)
        additional = []
        for follow_up in follow_up_images[:2]:
            extra_raw = await follow_up.read()
            additional.append(process_image(extra_raw, follow_up.content_type or "", get_settings().max_image_mb))
    except ValueError as exc:
        code = str(exc)
        if code == "too_large": raise HTTPException(413, "Please upload a smaller image.")
        if code == "unsupported_type": raise HTTPException(415, "Use JPG, PNG, or WebP.")
        raise HTTPException(400, "This image could not be read. Try another JPG, PNG, or WebP.")
    try: return await analyze_accessibility(image_bytes, mime_type, place_type, perspective, location_description, additional)
    except GeminiServiceError as exc:
        if str(exc) == "not_configured": raise HTTPException(503, "AI service is not configured.")
        raise HTTPException(502, "Analysis failed safely. Please retry.")
