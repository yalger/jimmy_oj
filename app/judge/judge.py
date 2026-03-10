from typing import Tuple

from app.judge.runner import run_python

def judge(code: str, input_data: str, expected_output: str) -> Tuple[str, str]:

    result = run_python(code, input_data)

    if result.get("timeout"):
        return "Time Limit Exceeded", ""

    if result["returncode"] != 0:
        return "Runtime Error", result["stderr"]

    output = result["stdout"].strip()

    if output == expected_output.strip():
        return "Accepted", output
    else:
        return "Wrong Answer", output