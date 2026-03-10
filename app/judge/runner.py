import subprocess
import uuid
from pathlib import Path


SUBMISSION_DIR = Path("submissions")


def run_python(code: str, input_data: str) -> dict:

    file_id = str(uuid.uuid4())
    file_path = SUBMISSION_DIR / f"{file_id}.py"

    with open(file_path, "w") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ["python", str(file_path)],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=2
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except subprocess.TimeoutExpired:
        return {
            "timeout": True
        }