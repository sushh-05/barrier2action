import io
from PIL import Image, ImageOps

try:
    import pillow_avif  # Registers AVIF support with Pillow.
except ImportError:
    pillow_avif = None

ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/webp", "image/avif"}

def process_image(image_bytes: bytes, mime_type: str, max_mb: int) -> tuple[bytes, str]:
    if mime_type not in ALLOWED_MIME_TYPES: raise ValueError("unsupported_type")
    if not image_bytes: raise ValueError("empty")
    if len(image_bytes) > max_mb * 1024 * 1024: raise ValueError("too_large")
    try:
        with Image.open(io.BytesIO(image_bytes)) as source:
            image = ImageOps.exif_transpose(source).convert("RGB")
            image.thumbnail((1400, 1400), Image.Resampling.LANCZOS)
            output = io.BytesIO(); image.save(output, format="JPEG", quality=82, optimize=True)
            return output.getvalue(), "image/jpeg"
    except Exception as exc: raise ValueError("unreadable") from exc
