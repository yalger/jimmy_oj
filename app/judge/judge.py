from app.judge.runner import run_program
from app.models.testcase import Testcase
    
def judge_problem(problem_id, code, language, db):

    testcases = db.query(Testcase).filter(
        Testcase.problem_id == problem_id
    ).all()

    for tc in testcases:

        result = run_program(
            code,
            language,
            tc.input_data
        )

        match(result["status"]):
            case "CE":
                return result
            case "TLE" | "MLE" | "RE":
                result["tc_id"] = tc.id
                return result
            case "OK":
                output = result["output"].strip()
                if output != tc.output_data.strip():
                    result["status"] = "WA"
                    result["tc_id"] = tc.id
                    return result
        print(result)

    result["status"] = "AC"
    return result