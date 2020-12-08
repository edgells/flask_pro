from celery import Celery

app = Celery("flask gunicorn")
