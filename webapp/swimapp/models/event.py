'''Classes related to Event'''
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin
from swimapp.models.stroke import Stroke
from swimapp.models.meet_event import MeetEventInline
from swimapp.models.choices_constants import (GENDER_CHOICES,
                                              DISTANCE_UNIT_CHOICES,
                                              EVENT_CODES)


class EventManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to events'''

    def get_queryset(self):
        '''Override manager to use select realted'''
        return super(EventManager, self).get_queryset() \
            .select_related('stroke')

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class Event(models.Model):
    '''Event info'''
    event_name = models.CharField(max_length=100)
    lower_age = models.IntegerField()
    upper_age = models.IntegerField()
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES)
    stroke = models.ForeignKey(Stroke)
    distance = models.IntegerField()
    distance_units = models.CharField(max_length=1,
                                      choices=DISTANCE_UNIT_CHOICES)
    is_relay = models.BooleanField(default=False)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    @property
    def hyv_line(self):
        '''Generate the event line for a hyv file'''
        line = str(self.id)
        line += ';F'  # Masters
        line += ';' + self.gender
        line += ';' + 'R' if self.is_relay else 'I'
        line += ';' + str(self.lower_age)
        line += ';' + str(self.upper_age)
        line += ';' + str(self.distance)
        line += ';' + str(EVENT_CODES[self.stroke.type_abbr])
        line += ';;;;0;;;;;;'

        return line

    @property
    def distance_text(self):
        '''combine distance and distanct_units to string'''
        return str(self.distance) + self.distance_units

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


class EventAdmin(admin.ModelAdmin):  # pylint: disable=R0904
    '''Add inline edit for Events'''
    inlines = (MeetEventInline,)
