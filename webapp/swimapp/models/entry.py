'''Classes related to entry in a entry'''

# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=W0142
# # Used * or ** magic
# pylint: disable=R0201
# # Method could be a function
# pylint: disable=C0103
# # Invalid property name

from django.contrib import admin
from django.db import models
from swimapp.models.meet_event import MeetEvent
from swimapp.models.athlete_entry import AthleteEntryInline
from swimapp.models.dq import DQ
from swimapp.models.finish_place import FinishPlace


class EntryManager(models.Manager):
    '''Static classes related to entries'''

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def get_queryset(self):
        '''Override manager to use select realted'''
        return super(EntryManager, self).get_queryset() \
            .select_related('meetevent', 'meetevent__event')

    def create_from_serializer(self, entry, validated_data):
        '''create entry from upload serializer dictionary'''
        dq_set_data = validated_data.pop('dq_set')
        finishplace_set_data = validated_data.pop('finishplace_set')

        dq_set = []
        for dq_data in dq_set_data:
            dq = DQ.objects.create_from_serializer(dq_data, entry)
            dq_set.append(dq)

        finishplace_set = []
        for finishplace_data in finishplace_set_data:
            finishplace = FinishPlace.objects.create_from_serializer(
                finishplace_data, entry)
            finishplace_set.append(finishplace)

        entry.lane_number = validated_data.get('lane_number',
                                               entry.lane_number)
        entry.result_time = validated_data.get('result_time',
                                               entry.result_time)
        entry.heat = validated_data.get('heat', entry.heat)
        entry.score = validated_data.get('score', entry.score)
        entry.scoring_heat = validated_data.get('scoring_heat',
                                                entry.scoring_heat)
        entry.save()

        return entry


class Entry(models.Model):
    '''Entry info'''
    lane_number = models.IntegerField(
        blank=True,
        null=True)
    result_time = models.FloatField(
        blank=True,
        null=True)
    seed_time = models.FloatField(
        blank=True,
        null=True)
    heat = models.IntegerField(
        blank=True,
        null=True)
    override_order = models.IntegerField(
        blank=True,
        null=True)
    score = models.IntegerField(
        blank=True,
        null=True)
    scoring_heat = models.BooleanField(default=False)
    meetevent = models.ForeignKey(MeetEvent)
    athletes = models.ManyToManyField('Athlete', through='AthleteEntry')
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = EntryManager()  # pylint: disable=E1120

    class Meta(object):
        '''Meta for model to be used by django'''
        # pylint: disable=R0903
        app_label = 'swimapp'

    def __unicode__(self):
        # pylint: disable=E1101
        return (self.meetevent.event.event_name +
                str(self.heat) + ", Lane " +
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
