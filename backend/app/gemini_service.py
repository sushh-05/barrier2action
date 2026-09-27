import logging
from app.config import get_settings
from app.prompts import build_prompt
from app.schemas import AuditResult
from app.validators import validate_audit_consistency
logger = logging.getLogger(__name__)
class GeminiServiceError(RuntimeError): pass
async def analyze_accessibility(image_bytes: bytes, mime_type: str, place_type: str, perspective: str, description: str, additional_images: list[tuple[bytes, str]] | None = None) -> AuditResult:
    settings = get_settings()
    if not settings.gemini_api_key or settings.gemini_api_key.startswith("your_"): raise GeminiServiceError("not_configured")
    try:
        from google import genai
        from google.genai import types
        client = genai.Client(api_key=settings.gemini_api_key)
        contents = [types.Part.from_bytes(data=image_bytes, mime_type=mime_type)]
        for extra_bytes, extra_mime in (additional_images or [])[:2]:
            contents.append(types.Part.from_bytes(data=extra_bytes, mime_type=extra_mime))
        contents.append(build_prompt(place_type, perspective, description))
        response = client.models.generate_content(
            model=settings.gemini_model,
            contents=contents,
            config=types.GenerateContentConfig(response_mime_type="application/json", response_schema=AuditResult, temperature=0.2, max_output_tokens=1400),
        )
        return validate_audit_consistency(AuditResult.model_validate_json(response.text))
    except GeminiServiceError: raise
    except Exception as exc:
        logger.exception("Gemini audit failed"); raise GeminiServiceError("analysis_failed") from exc
