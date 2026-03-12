from pydantic import BaseModel, Field

class AddProblemRequest(BaseModel):
    title: str = Field(max_length=255)
    description: str
    time_limit: int