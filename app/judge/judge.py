from sqlalchemy.orm import Session

from app.judge.runner import run_python
from app.models.testcase import Testcase
    
def judge_problem(problem_id: int, code: str, db: Session):

    testcases = db.query(Testcase).filter(
        Testcase.problem_id == problem_id
    ).all()

    for tc in testcases:

        result = run_python(code, tc.input_data)

        if result.get("timeout"):
            return "TLE"

        output = result["stdout"].strip()

        if output != tc.output_data.strip():
            return "WA"

    return "AC"