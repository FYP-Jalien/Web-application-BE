from fastapi import APIRouter
from services.tests_service import TestService

router = APIRouter(prefix="/tests", tags=["tests"])


@router.get("/")
async def run_tests():
    return TestService().start_tests()
