'''Classes related to Meet'''
import re
from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.contrib import admin
from .athlete import Athlete
from .meet_type import MeetType
from .meet_config import MeetConfig
from .course_code import CourseCode
from .event import Event
from .meet_event import MeetEvent
from .meet_event import MeetEventInline
from .team import Team
from .facility import Facility


class MeetManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to meets'''

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def meets_for_team(self, team):  # pylint: disable=E1002
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
    meet_config = models.ForeignKey(MeetConfig, null=True)
    team = models.ForeignKey(Team, null=True)
    teams = models.ManyToManyField(Team, related_name='all_meet_set')
    events = models.ManyToManyField(Event, through=MeetEvent)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = MeetManager()  # pylint: disable=E1120

    class Meta:  # pylint: disable=W0232,C1001,R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'
        unique_together = ('meet_name', 'start_date',)

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.meet_name

    def get_absolute_url(self):  # pylint: disable=E0202
        '''Get reverse url for meets'''
        # pylint: disable=E1101
        return reverse('swimapp_view_meet', args=[self.id])

    @property
    def athletes_for_meet(self):
        '''Return distict list of athletes that are related to this meet'''
        # pylint: disable=E1101
        return Athlete.objects.filter(
            entry__event__meet=self.id).distinct()


class MeetAdmin(admin.ModelAdmin):  # pylint: disable=R0904
    '''Add inline editing for meet events'''
    inlines = (MeetEventInline,)
