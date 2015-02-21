'''Classes related to Meet'''

# pylint: disable=too-many-public-methods
# pylint: disable=too-few-public-methods
# pylint: disable=no-member
# pylint: disable=no-value-for-parameter
# pylint: disable=super-on-old-class

import re
from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.contrib import admin
from swimapp.models.athlete import Athlete
from swimapp.models.meet_type import MeetType
from swimapp.models.meet_config import MeetConfig
from swimapp.models.course_code import CourseCode
from swimapp.models.event import Event
from swimapp.models.meet_event import MeetEvent
from swimapp.models.meet_event import MeetEventInline
from swimapp.models.team import Team
from swimapp.models.facility import Facility
from swimapp.models.violation import Violation


class MeetManager(models.Manager):
    '''Static classes related to meets'''

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def get_queryset(self):
        '''Override manager to use select realted'''
        return super(MeetManager, self).get_queryset() \
            .select_related('meet_type', 'course_code_1', 'course_code_2',
                            'meet_config', 'team', 'teams', 'events')

    def meets_for_team(self, team):
        '''Return a queryset for meets that belong to a team'''
        return super(MeetManager, self).get_queryset().filter(Q(team=team.id))


class Meet(models.Model):
    '''Meet info'''
    name_regex = re.compile(r'^[A-Za-z0-9\-\_]+$')
    name_validator = RegexValidator(regex=name_regex)
    meet_name = models.CharField(max_length=45,
                                 validators=[name_validator])
    facility = models.ForeignKey(Facility)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    age_up_date = models.DateField(blank=True, null=True)
    meet_masters = models.BooleanField(default=False)
    meet_type = models.ForeignKey(MeetType,
                                  related_name='meet_type_set',
                                  null=True)
    course_code_1 = models.ForeignKey(CourseCode,
                                      related_name='course_code_1_set',
                                      null=True)
    course_code_2 = models.ForeignKey(CourseCode,
                                      related_name='course_code_2_set',
                                      blank=True,
                                      null=True)
    lane_count = models.IntegerField(blank=True, null=True)
    max_indiv_entries = models.IntegerField(blank=True, null=True)
    max_relay_entries = models.IntegerField(blank=True, null=True)
    max_entries = models.IntegerField(blank=True, null=True)
    meet_config = models.ForeignKey(MeetConfig, null=True)
    team = models.ForeignKey(Team, null=True)
    teams = models.ManyToManyField(Team, related_name='all_meet_set')
    events = models.ManyToManyField(Event, through=MeetEvent)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = MeetManager()

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'
        unique_together = ('meet_name', 'start_date',)

    def __unicode__(self):
        '''
        Define the __unicode__ method, which is used by related models
        by default.
        '''
        return self.meet_name

    def get_absolute_url(self):
        '''Get reverse url for meets'''
        return reverse('swimapp_view_meet', args=[self.id])

    @property
    def athletes_for_meet(self):
        '''Return distinct list of athletes that are related to this meet'''
        return Athlete.objects.prefetch_related().filter(
            entry__meetevent__meet=self.id).distinct()

    @property
    def teams_for_meet(self):
        '''Return distinct list of teams that are related to this meet'''
        return Team.objects.prefetch_related().filter(
            Q(meet=self) | Q(all_meet_set__team=self.team.id)
            ).distinct()

    @property
    def violations_for_meet(self):
        '''Return distict list of violations that are related to the meet'''
        return Violation.objects.prefetch_related().filter(
            # meetviolation__meet=self.id
            Q(meets=self)
            ).distinct()


class MeetAdmin(admin.ModelAdmin):
    '''Add inline editing for meet events'''
    inlines = (MeetEventInline,)
