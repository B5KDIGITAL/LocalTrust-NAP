from fastapi import APIRouter
from pydantic import BaseModel
from models.business import NAPData
from services.browser_service import inject_nap_data

router = APIRouter(
    prefix="/injection",
    tags=["injection"],
)

class InjectionRequest(BaseModel):
    nap_data: NAPData
    directory_url: str

@router.post("/start")
async def start_injection(request: InjectionRequest):
    """
    Start a NAP injection process for a given business and directory URL.
    """
    result = await inject_nap_data(request.nap_data, request.directory_url)
    return {"message": "Injection task completed", "result": result}
