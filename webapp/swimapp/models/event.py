'''Classes related to Event'''
from django.db import models
from .stroke import Stroke
from .meet import Meet


class Event(models.Model):
    '''Event info'''
    event_name = models.CharField(max_length=30)
    event_number = models.IntegerField()
    meet = models.ForeignKey(Meet, related_name='events')
    lower_age = models.IntegerField()
    upper_age = models.IntegerField()
    stroke = models.ForeignKey(Stroke)
    distance = models.IntegerField()
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.event_name
