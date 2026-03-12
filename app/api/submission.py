from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.judge.judge import judge_problem
from app.models.submission import Submission
from app.schemas.submission import SubmitRequest, SubmitResponse

router = APIRouter(prefix="/submission", tags=["submission"])

@router.post("/submit", response_model=SubmitResponse)
def submit(
    request: Request,
    data: SubmitRequest,
    db: Session = Depends(get_db)
):

    submission = Submission(
        user_id=1,
        problem_id=data.problem_id,
        code=data.code,
        status="Running"
    )

    db.add(submission)
    db.commit()

    result = judge_problem(data.problem_id, data.code, db)

    submission.result = result
    submission.status = "Finished"
    db.commit()

    return submission