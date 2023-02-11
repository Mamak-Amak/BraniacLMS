import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

celery_app = Celery("braniac")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
<<<<<<< HEAD
<<<<<<< HEAD
celery_app.autodiscover_tasks()
<<<<<<< HEAD
=======
celery_app.autodiscover_tasks()
>>>>>>> lesson_7 Email via celery
=======
celery_app.autodiscover_tasks()
>>>>>>> Lesson 6 (#5)
=======
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
>>>>>>> lesson_7 Email via celery
