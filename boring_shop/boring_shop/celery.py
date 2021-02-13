import os
from celery import Celery

#Set the default django settings modules for celery program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE','boring_shop.settings')

app = Celery('boring_shop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()