from app.judge.testcase_loader import load_testcases
from app.judge.runner import run_program
from app.models.problem import Problem
    
def judge_problem(problem: Problem, code, language):

    testcases = load_testcases(problem)

    for i, (input_data, expected_output) in enumerate(testcases):

        result = run_program(
            code,
            language,
            input_data
        )

        match(result["status"]):
            case "CE":
                return result
            case "TLE" | "MLE" | "RE":
                result["tc_id"] = i + 1
            case "OK":
                output = result["output"].strip()
                if output != expected_output.strip():
                    result["status"] = "WA"
                    result["tc_id"] = i + 1
                else:
                    result["status"] = "AC"

    return result