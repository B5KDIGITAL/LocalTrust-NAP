from supabase import create_client, Client
from core.config import settings
import logging

logger = logging.getLogger(__name__)

def get_supabase_client() -> Client | None:
    if not settings.supabase_url or not settings.supabase_key:
        logger.warning("Supabase URL or Key not set. Supabase client will not be initialized.")
        return None
    try:
        return create_client(settings.supabase_url, settings.supabase_key)
    except Exception as e:
        logger.error(f"Failed to initialize Supabase client: {e}")
        return None
