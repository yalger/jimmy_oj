import os

from celery import Celery


redis_url = f"redis://{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}/{os.getenv('REDIS_DB')}"

celery_app = Celery(
    "jimmy_oj",
    broker=redis_url,
    backend=redis_url
)