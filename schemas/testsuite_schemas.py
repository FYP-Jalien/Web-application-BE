from pydantic import BaseModel


class TestSummarySchema(BaseModel):
    id: str
    name: str
    status: str
    level: str
    message: str
