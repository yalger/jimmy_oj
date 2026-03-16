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

cmd = [
    "/usr/bin/time",
    "-f",
    "%e %M"
] + run_cmd

try:
    result = subprocess.run(
        cmd,
        input=input_data,
        capture_output=True,
        text=True,
        timeout=5
    )

except subprocess.TimeoutExpired:
    sys.stdout.write("STATUS:TLE")
    sys.exit(0)

if result.returncode != 0:
    if "Command terminated by signal 9" in result.stderr:
        sys.stdout.write("STATUS:MLE")
    else:
        sys.stdout.write("STATUS:RE")
        sys.stderr.write('\n'.join(result.stderr.split("\n")[:-2]))
    sys.exit(0)

lines = result.stderr.strip().split()

time_used = int(float(lines[0]) * 1000)
memory_used = int(lines[1])

sys.stdout.write("STATUS:OK\n")
sys.stdout.write(f"TIME:{time_used}\n")
sys.stdout.write(f"MEMORY:{memory_used}")
sys.stderr.write(result.stdout)