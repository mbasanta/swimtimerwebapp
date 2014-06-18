'''Classes related to Meet'''
from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import admin
from localflavor.us.models import USStateField
from .meet_type import MeetType
from .meet_config import MeetConfig
from .course_code import CourseCode
from .event import Event
from .meet_event import MeetEvent
from .meet_event import MeetEventInline
from .team import Team


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
    meet_name = models.CharField(max_length=45)
    facility = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    age_up_date = models.DateField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    meet_type_1 = models.ForeignKey(MeetType,
                                    related_name='meet_type_1_set')
    meet_type_2 = models.ForeignKey(MeetType,
                                    related_name='meet_type_2_set',
                                    blank=True,
                                    null=True)
    course_code_1 = models.ForeignKey(CourseCode,
                                      related_name='course_code_1_set')
    course_code_2 = models.ForeignKey(CourseCode,
                                      related_name='course_code_2_set',
                                      blank=True,
                                      null=True)
    meet_config = models.ForeignKey(MeetConfig)
    addr_name = models.CharField(max_length=30, blank=True, null=True)
    addr = models.CharField(max_length=30, blank=True, null=True)
    addr_city = models.CharField(max_length=30, blank=True, null=True)
    addr_state = USStateField(blank=True, null=True)
    addr_zip = models.CharField(max_length=10, blank=True, null=True)
    addr_country = models.CharField(max_length=3, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    team = models.ForeignKey(Team)
    events = models.ManyToManyField(Event, through=MeetEvent)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = MeetManager()  # pylint: disable=E1120

    class Meta:  # pylint: disable=W0232,C1001,R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.meet_name

    def get_absolute_url(self):  # pylint: disable=E0202
        '''Get reverse url for meets'''
        # pylint: disable=E1101
        return reverse('swimapp_view_meet', args=[self.id])


class MeetAdmin(admin.ModelAdmin):  # pylint: disable=R0904
    '''Add inline editing for meet events'''
    inlines = (MeetEventInline,)
