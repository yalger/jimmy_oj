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
        submission.code,
        db
    )

    submission.status = "Finished"
    submission.result = result
    db.commit()

    db.close()