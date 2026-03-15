from pydantic import BaseModel

class SubmitRequest(BaseModel):
    problem_id: int
    language: str
    code: str