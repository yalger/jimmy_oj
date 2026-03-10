from fastapi import FastAPI

from app.judge.judge import judge
from app.schemas.submit import SubmitRequest, SubmitResponse

app = FastAPI(title="Jimmy OJ")


@app.post("/submit", response_model=SubmitResponse)
def submit(req: SubmitRequest):

    status, output = judge(
        req.code,
        req.input,
        req.expected_output
    )

    return SubmitResponse(
        status=status,
        output=output
    )