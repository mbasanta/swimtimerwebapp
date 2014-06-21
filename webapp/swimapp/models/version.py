'''Classes related to stroke'''
from django.db import models


class VersionManager(models.Manager):  # pylint: disable=R0904
    '''Static classes for version'''

    class Meta(object):  # pylint: disable=C1001, W0232, R0903
        '''Meta info for Django model'''
        app_label = 'swimapp'

    def latest_version(self):
        '''Return lastest version'''
        return super(VersionManager, self).get_queryset().last()


class Version(models.Model):
    '''Application Version'''
    version = models.IntegerField()
    datetime = models.DateTimeField()
    objects = VersionManager()

    class Meta(object):  # pylint: disable=C1001, W0232, R0903
        '''Meta info for Django model'''
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return 'Version ' + str(self.version)
