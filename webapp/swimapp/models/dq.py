'''Classes related to a DQ'''

# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=E1120
# # No value in constructor call

from django.db import models
from swimapp.models.entry import Entry
from swimapp.models.judge import Judge


class DQManager(models.Manager):
    '''Static classes related to dqs'''

    def get_queryset(self):
        '''Override manager to use select related'''
        return super(DQManager, self).get_queryset() \
            .select_related('entry')

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class DQ(models.Model):
    '''DQ info'''
    reason = models.CharField(max_length=500)
    entry = models.ForeignKey(Entry)
    judge = models.ForeignKey(Judge)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = DQManager()

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        '''
        Define the __unicode__ method, which is used by related
        models by default.
        '''
        return unicode(self.reason)
