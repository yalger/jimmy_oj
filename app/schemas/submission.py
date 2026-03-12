from pydantic import BaseModel

from app.api import submission


class SubmitRequest(BaseModel):
    problem_id: int
    code: str


class SubmitResponse(BaseModel):
    id: int
    user_id: int
    problem_id: int
    status: str
    result: str