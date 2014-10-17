from __future__ import absolute_import

from celery import shared_task
from swimapp.models.fileupload import FileUpload


@shared_task
def process_hy3_upload(file_id):
    hy3file = FileUpload.objects.get(id=file_id)
    hy3file.process()
