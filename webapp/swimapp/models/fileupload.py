'''Classes related to Team'''
from django.conf import settings
from django.db import models
from django.db.models import Q
from swimapp.models.choices_constants import FILE_UPLOAD_CHOICES


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
    filename = models.CharField(max_length=100)
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
