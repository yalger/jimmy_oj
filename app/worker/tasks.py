from app.worker.celery_app import celery_app
from app.db.database import SessionLocal
from app.judge.judge import judge_problem
from app.models.submission import Submission

from app.models import problem, submission, testcase, user

@celery_app.task
def judge_submission(submission_id):

    db = SessionLocal()

    submission = db.query(Submission).get(submission_id)

    submission.status = "Running"
    db.commit()

    result = judge_problem(
        submission.problem_id,
        submission.language,
        submission.code,
        db
    )

    submission.status = result["status"]
    match(submission.status):
        case "CE":
            submission.wrong_output = result["output"]
        case "TLE" | "MLE":
            submission.wrong_tc_id = result["tc_id"]
        case "RE" | "WA":
            submission.wrong_tc_id = result["tc_id"]
            submission.wrong_output = result["output"]
    db.commit()

    db.close()