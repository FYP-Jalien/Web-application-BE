from pydantic import BaseModel


class ContainerInformationSchema(BaseModel):
    container_name: str
    image: str
    uptime: str
    status: str


class ContainerSchema(BaseModel):
    container_information: list[ContainerInformationSchema] = None
    error: str = None
