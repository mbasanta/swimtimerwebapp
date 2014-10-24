'''Classes related to Team'''
from datetime import datetime
from django.conf import settings
from django.db import models
from django.db.models import Q
from hy3parser.hy3Parser import Hy3Parser


class FileUploadManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to teams'''

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def files_for_user(self, appuser):  # pylint: disable=E1002
        '''Return a queryset of files that below to a user'''
        return super(FileUploadManager, self).get_queryset().filter(
            Q(appuser=appuser)
        )


class FileUpload(models.Model):
    '''Uploaded File'''
    # pylint: disable=C0330
    # pylint: disable=W0703
    #   Too general an exception
    # pylint: disable=E1101
    #   Instance of abc has not member xyz

    PENDING, PROCESSED, FAILED = 'Pending', 'Processed', 'Failed'
    STATUSES = (
        (PENDING, PENDING),
        (PROCESSED, PROCESSED),
        (FAILED, FAILED)
    )

    HY3_FILE = 'hy3_file'
    OTHER = 'other'
    FILE_UPLOAD_CHOICES = (
        (HY3_FILE, 'HY3 File'),
        (OTHER, 'Other'),
    )

    filename = models.CharField(max_length=100)
    status = models.CharField(max_length=30, choices=STATUSES, default=PENDING)
    processing_description = models.TextField(blank=True, null=True)
    time_start_processing = models.DateTimeField(blank=True, null=True)
    time_end_processing = models.DateTimeField(blank=True, null=True)
    filetype = models.CharField(
        max_length=25,
        choices=FILE_UPLOAD_CHOICES)
    docfile = models.FileField(
        upload_to='documents/%Y/%m/%d/%H/%M/%S',
        max_length=300)
    appuser = models.ForeignKey(settings.AUTH_USER_MODEL)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = FileUploadManager()  # pylint: disable=E1120

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        return self.filename

    def process(self):
        '''Process the uploaded file, only hy3 files right now'''
        self.time_start_processing = datetime.now()
        try:
            Hy3Parser.parse_file(self.docfile.path)
        except Exception, error:
            self._mark_failed(unicode(error))
        else:
            self._mark_processed()

    def _mark_processed(self, description=None):
        '''protected method that sets end time and marks file as processed'''
        self.status = self.PROCESSED
        self.time_end_processing = datetime.now()
        self.processing_description = description
        self.save()

    def _mark_failed(self, description):
        '''
        protected method marks file and complete and sets processing
        desciption
        '''
        self.status = self.FAILED
        self.processing_description = description
        self.save()

    def was_processing_successful(self):
        '''checks the status of file processing'''
        return self.status == self.PROCESSED
