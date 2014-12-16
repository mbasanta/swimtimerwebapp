'''Classes related to Event'''

# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=E1120
# # No value in constructor call

from django.db import models
from swimapp.models.entry import Entry
from swimapp.models.judge import Judge
from swimapp.models.choices_constants import (RESULT_TYPES)


class ResultManager(models.Manager):
    '''Static classes related to results'''

    def get_queryset(self):
        '''Override manager to use select related'''
        return super(ResultManager, self).get_queryset() \
            .select_related('entry')

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class Result(models.Model):
    '''Result info'''
    timestamp = models.DateTimeField()
    result_type = models.CharField(
        max_length=25,
        choices=RESULT_TYPES)
    entry = models.ForeignKey(Entry)
    timer = models.ForeignKey(Judge)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = ResultManager()

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        '''
        Define the __unicode__ method, which is used by related
        models by default.
        '''
        return self.timestamp
