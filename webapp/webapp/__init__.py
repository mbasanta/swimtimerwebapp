""" webapp """
from __future__ import absolute_import

# This makes sure the app is already imported when
# Django starts so that shared_tasks will use it
from webapp.celery import app as celery_app
