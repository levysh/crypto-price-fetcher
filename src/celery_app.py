from celery import Celery

from src.config import settings

app = Celery("worker", backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER_URL)

# TODO: find better way for celery tasks discovery
app.autodiscover_tasks(["src.currency"], related_name="celery", force=True)
