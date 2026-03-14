import subprocess
import uuid
from pathlib import Path

SUBMISSION_DIR = Path("submissions")


def run_python(code, input_data):

    uid = str(uuid.uuid4())

    workdir = SUBMISSION_DIR / uid
    workdir.mkdir()

    code_file = workdir / "main.py"
    input_file = workdir / "input.txt"

    with open(code_file, "w") as f:
        f.write(code)

    with open(input_file, "w") as f:
        f.write(input_data)

    cmd = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{workdir.absolute()}:/app/work",
        "--network",
        "none",
        "--memory",
        "256m",
        "--cpus",
        "1",
        "jimmy_oj_sandbox"
    ]

    try:

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except subprocess.TimeoutExpired:
        return {"timeout": True}