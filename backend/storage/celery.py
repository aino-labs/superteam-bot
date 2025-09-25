from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from config import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storage.settings')

app = Celery('storage')

app.conf.broker_url = env.env_required('CELERY_BROKER_URL')
app.conf.result_backend = env.env_required('CELERY_RESULT_BACKEND')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
print(app.tasks)