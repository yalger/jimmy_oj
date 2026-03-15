import json
import os
import subprocess
import sys

os.chdir("/app/work")

CONFIG_FILE = "/app/work/config.json"
INPUT_FILE = "/app/work/input.txt"

with open(CONFIG_FILE) as f:
    config = json.load(f)

compile_cmd = config["compile"]
run_cmd = config["run"]

if compile_cmd:

    compile_result = subprocess.run(
        compile_cmd,
        capture_output=True,
        text=True
    )

    if compile_result.returncode != 0:
        sys.stdout.write("STATUS:CE")
        sys.stderr.write(compile_result.stderr)
        sys.exit(0)

with open(INPUT_FILE, "r") as f:
    input_data = f.read()

try:
    result = subprocess.run(
        run_cmd,
        input=input_data,
        capture_output=True,
        text=True,
        timeout=5
    )

except subprocess.TimeoutExpired:
    sys.stdout.write("STATUS:TLE")
    sys.exit(0)

if result.returncode != 0:
    sys.stdout.write("STATUS:RE")
    sys.stderr.write(result.stderr)
    sys.exit(0)

sys.stdout.write("STATUS:OK")
sys.stderr.write(result.stdout)