from pathlib import Path
import os

from app.models.problem import Problem

DATA_DIR = Path(os.getenv("DATA_DIR"))

def load_testcases(problem: Problem):

    data_dir = DATA_DIR / problem.data_path

    testcases = []

    i = 1

    while True:

        input_file = data_dir / f"{i}.in"
        output_file = data_dir / f"{i}.out"

        if not input_file.exists():
            break

        with open(input_file) as f:
            input_data = f.read()

        with open(output_file) as f:
            output_data = f.read()

        testcases.append((input_data, output_data))

        i += 1

    return testcases