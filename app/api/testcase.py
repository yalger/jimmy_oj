from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request

from app.dependencies.database import get_db
from app.models.testcase import Testcase
from app.schemas.response import APIResponse
from app.schemas.testcase import AddTestcaseRequest

router = APIRouter(prefix="/testcase", tags=["testcase"])

@router.post("/add", response_model=APIResponse)
def add_testcase(
    request: Request,
    data: AddTestcaseRequest,
    db: Session = Depends(get_db)
):
    testcases = db.query(Testcase).filter_by(problem_id=data.problem_id).all()
    tc_num = len(testcases)

    new_tc = Testcase(
        problem_id=data.problem_id,
        tc_num = tc_num + 1,
        input_data=data.input_data,
        output_data=data.output_data
    )

    db.add(new_tc)
    db.commit()
    db.refresh(new_tc)

    return APIResponse(
        success=True,
        message="Testcase added successfully",
        data={
            "problem_id": new_tc.problem_id,
            "tc_num": new_tc.tc_num
        }
    )