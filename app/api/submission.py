from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.models import submission
from app.models.submission import Submission
from app.schemas.response import APIResponse
from app.schemas.submission import SubmitRequest
from app.worker.tasks import judge_submission

router = APIRouter(prefix="/submission", tags=["submission"])

@router.get("/{submission_id}", response_model=APIResponse)
def get_submission(
    request: Request,
    submission_id: int,
    db: Session = Depends(get_db)
):
    submission = db.query(Submission).get(submission_id)

    if not submission:
        return APIResponse(
            success=False,
            message="Submission not found"
        )

    return APIResponse(
        success=True,
        message="Submission found",
        data={
            "submission_id": submission.id,
            "user_id": submission.user_id,
            "problem_id": submission.problem_id,
            "status": submission.status,
            "result": submission.result
        }
    )

@router.post("/submit", response_model=APIResponse)
def submit(
    request: Request,
    data: SubmitRequest,
    db: Session = Depends(get_db)
):

    submission = Submission(
        user_id=1,
        problem_id=data.problem_id,
        code=data.code,
        status="Pending"
    )

    db.add(submission)
    db.commit()
    db.refresh(submission)

    judge_submission.delay(submission.id)

    return APIResponse(
        success=True,
        message="Successfully submitted",
        data={
            "submission_id": submission.id,
            "user_id": submission.user_id,
            "problem_id": submission.problem_id,
            "status": submission.status,
            "result": submission.result
        }
    )