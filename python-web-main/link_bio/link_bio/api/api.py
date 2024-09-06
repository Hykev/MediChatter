import link_bio.constants as const
from link_bio.model.Featured import Featured
from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()


async def repo() -> str:
    return const.REPO_URL

async def featured() -> list[Featured]:
    return SUPABASE_API.featured()