from functools import lru_cache
import os
from pathlib import Path


def _load_dotenv() -> None:
    env_file = Path(__file__).resolve().parents[1] / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())


class Settings:
    def __init__(self):
        _load_dotenv()
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")
        self.gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
        self.max_image_mb = int(os.getenv("MAX_IMAGE_MB", "8"))
        self.host = os.getenv("HOST", "0.0.0.0")
        self.port = int(os.getenv("PORT", "8000"))

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.frontend_origin.split(",") if origin.strip()]


@lru_cache()
def get_settings() -> Settings:
    return Settings()
