from pydantic import BaseModel

class Inspection(BaseModel):
    site_name: str
    inspector: str
    date: str
    observations: list
