from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Setting the environment variable for project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Creating an instance of the Celery object
app = Celery('config')

# Loading settings from the Django configuration file
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically detecting and registering tasks from files named tasks.py in Django apps
app.autodiscover_tasks()

app.conf.timezone = 'UTC'
