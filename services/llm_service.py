from google import genai
from core.config import settings
import logging

logger = logging.getLogger(__name__)

def get_genai_client() -> genai.Client | None:
    if not settings.google_api_key:
        logger.warning("Google API Key not set. GenAI client will not be initialized.")
        return None
    try:
        return genai.Client(api_key=settings.google_api_key)
    except Exception as e:
        logger.error(f"Failed to initialize GenAI client: {e}")
        return None
