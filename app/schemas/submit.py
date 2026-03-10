from pydantic import BaseModel


class SubmitRequest(BaseModel):
    code: str
    input: str
    expected_output: str


class SubmitResponse(BaseModel):
    status: str
    output: str