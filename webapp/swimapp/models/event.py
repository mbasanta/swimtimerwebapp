'''Classes related to Event'''
from django.db import models
from django.core.urlresolvers import reverse
from .stroke import Stroke


class EventManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to events'''

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class Event(models.Model):
    '''Event info'''
    event_name = models.CharField(max_length=30)
    event_number = models.IntegerField()
    lower_age = models.IntegerField()
    upper_age = models.IntegerField()
    stroke = models.ForeignKey(Stroke)
    distance = models.IntegerField()
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = EventManager()  # pylint: disable=E1120

    class Meta:  # pylint: disable=W0232,C1001,R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.event_name

    def get_absolute_url(self):  # pylint: disable=E0202
        '''Get reverse url for events'''
        # pylint: disable=E1101
        return reverse('swimapp_view_event', args=[self.id])
