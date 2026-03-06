from pydantic import BaseModel

class InspectionObservation(BaseModel):
    description: str
    location: str
    hazard_type: str
