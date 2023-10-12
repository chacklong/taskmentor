from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO.SETTINGS.MODULE','taskmentor.settings')
app = Celery('taskmentor')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()