'''Classes related to Heat'''
from django.db import models
from .event import Event


class Heat(models.Model):
    '''Heat info'''
    heat_number = models.IntegerField()
    event = models.ForeignKey(Event, related_name='heats')
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        return self.event.event_name + ": Heat " + str(self.heat_number)
