'''Classes related to entry in a heat'''
from django.contrib import admin
from django.db import models
from .athlete_entry import AthleteEntryInline
from .heat import Heat
from .event import Event


class EntryManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to entries'''

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class Entry(models.Model):
    '''Entry info'''
    lane_number = models.IntegerField()
    result_time = models.FloatField()
    seed_time = models.FloatField()
    heat = models.ForeignKey(Heat)
    event = models.ForeignKey(Event)
    athletes = models.ManyToManyField('Athlete', through='AthleteEntry')
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    class Meta(object):
        '''Meta for model to be used by django'''
        # pylint: disable=R0903
        app_label = 'swimapp'

    def __unicode__(self):
        # pylint: disable=E1101
        return (self.heat.event.event_name + ", Heat " +
                str(self.heat.heat_number) + ", Lane " +
                str(self.lane_number))

    @property
    def result_min_sec(self):
        '''Result time as a list. [min, sec]'''
        return_time = []
        return_time.append(int(self.result_time / 60.0))
        return_time.append(round(((self.result_time / 60.0) % 1.0) * 60, 3))
        return return_time

    @result_min_sec.setter
    def time(self, time):
        '''Expects a list or tuple of (min, sec)'''
        if isinstance(time, (tuple, list)):
            self.result_time = (time[0] * 60) + time[1]
        else:
            raise ValueError


class EntryAdmin(admin.ModelAdmin):  # pylint: disable=R0904
    '''Add inline edit for Athletes'''
    inlines = (AthleteEntryInline,)