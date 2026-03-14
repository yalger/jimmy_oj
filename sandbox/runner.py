import subprocess
import sys

CODE_FILE = "/app/work/main.py"
INPUT_FILE = "/app/work/input.txt"

try:
    with open(INPUT_FILE, "r") as f:
        input_data = f.read()

    result = subprocess.run(
        ["python", "-u", CODE_FILE],
        input=input_data,
        capture_output=True,
        text=True,
        timeout=2
    )

    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)

except subprocess.TimeoutExpired:
    print("TIMEOUT")