'''Classes related to stroke'''
from django.db import models


class Version(models.Model):
    '''Application Version'''
    version = models.IntegerField()
    datetime = models.DateTimeField()

    class Meta:  # pylint: disable=C1001, W0232, R0903
        '''Meta info for Django model'''
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return 'Version ' + str(self.version)
