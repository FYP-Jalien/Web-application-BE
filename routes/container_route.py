from fastapi import APIRouter
from services.container_service import ContainerService

router = APIRouter(prefix="/container", tags=["container"])


@router.get("/status")
async def container_status():
    return ContainerService().check_status()


@router.get("/up")
async def container_up():
    return ContainerService().up_containers()


@router.get("/down")
async def container_down():
    return ContainerService().down_containers()


@router.get("/terminal/{container_id}")
async def container_terminal(container_id: str):
    return ContainerService().open_terminal(container_id)
