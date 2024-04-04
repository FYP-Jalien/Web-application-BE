from fastapi import APIRouter
from services.container_service import ContainerService

router = APIRouter(prefix="/container", tags=["container"])


@router.get("/status")
async def container_status():
    return ContainerService().check_status()

