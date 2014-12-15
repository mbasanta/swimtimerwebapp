'''Classes related to judge'''

# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=E1120
# # No value in constructor call

from django.conf import settings
from django.db import models


class JudgeManager(models.Manager):
    '''Static classes related to judge'''

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class Judge(models.Model):
    '''Judge info'''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True)
    username = models.CharField(
        max_length=50,
        blank=True,
        null=True)
    is_authenticated = models.BooleanField()
    is_override = models.BooleanField()
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = JudgeManager()

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        '''
        Define the __unicode__ method, which is used by related
        models by default.
        '''
        return self.username
