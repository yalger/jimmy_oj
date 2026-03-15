from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.models.problem import Problem
from app.schemas.problem import AddProblemRequest
from app.schemas.response import APIResponse

router = APIRouter(prefix="/problem", tags=["problem"])

@router.get("/all", response_model=APIResponse)
def problems(db: Session = Depends(get_db)):
    problems = db.query(Problem).all()

    return APIResponse(
        success=True,
        message="Successfully get all problems",
        data=[
            {
                "problem_id": problem.id,
                "title": problem.title,
                "description": problem.description,
            } for problem in problems
        ]
    )

@router.get("/{title}", response_model=APIResponse)
def problem_by_title(
    title: str,
    db: Session = Depends(get_db)
):
    problem = db.query(Problem).filter_by(title=title).first()

    if not problem:
        return APIResponse(
            success=False,
            message="Problem not found"
        )

    return APIResponse(
        success=True,
        message="Successfully get problem",
        data={
            "problem_id": problem.id,
            "title": problem.title,
            "description": problem.description,
        }
    )

@router.post("/add", response_model=APIResponse)
def add_problem(
    request: Request,
    data: AddProblemRequest,
    db: Session = Depends(get_db)
):
    problem = Problem(
        title=data.title,
        description=data.description,
    )

    db.add(problem)
    db.commit()
    db.refresh(problem)

    return APIResponse(
        success=True,
        message="Problem added successfully",
        data={
            "problem_id": problem.id
        }
    )