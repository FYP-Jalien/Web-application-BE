from fastapi import APIRouter
from services.container_service import ContainerService
import subprocess

router = APIRouter(prefix="/container", tags=["container"])


@router.get("/status")
async def container_status():
    result, error = ContainerService().check_status()
    return {"output": result, "error": result.stderr}
