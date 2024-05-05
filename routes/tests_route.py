from fastapi import APIRouter
from services.tests_service import TestService

router = APIRouter(prefix="/tests", tags=["tests"])


@router.get("/")
async def run_tests():
    return TestService().start_tests()


@router.get("/stop/{pid}")
async def stop_tests(pid: int):
    return TestService().stop_tests(pid)


@router.get("/summary")
async def read_summary():
    return TestService().read_test_summary()
