import json
from pathlib import Path
import subprocess
import uuid

from app.judge.languages import LANGUAGES

SUBMISSION_DIR = Path("submissions")

def run_program(language, code, input_data):

    uid = str(uuid.uuid4())

    workdir = SUBMISSION_DIR / uid
    workdir.mkdir()

    lang = LANGUAGES[language]

    code_file = workdir / lang["filename"]
    input_file = workdir / "input.txt"
    config_file = workdir / "config.json"

    with open(code_file, "w") as f:
        f.write(code)

    with open(input_file, "w") as f:
        f.write(input_data)

    config = {
        "compile": lang["compile"],
        "run": lang["run"]
    }

    with open(config_file, "w") as f:
        json.dump(config, f)

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
        "--pids-limit",
        "64",
        "jimmy_oj_sandbox"
    ]

    try:

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10
        )

    except subprocess.TimeoutExpired:
        return {
            "status": "TLE"
        }

    match(result.stdout.strip()):
        case "STATUS:CE":
            return {
                "status": "CE",
                "output": result.stderr
            }
        case "STATUS:TLE":
            return {
                "status": "TLE"
            }
        case "STATUS:RE":
            return {
                "status": "RE",
                "output": result.stderr
            }
        case "STATUS:OK":
            return {
                "status": "OK",
                "output": result.stderr
            }
    if result.returncode == 137:
        return {"status": "MLE"}
    print(result)
    return {"status": "UNKNOWN"}