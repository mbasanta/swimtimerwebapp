'''Classes related to Team'''

# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=E1120
# # No value in constructor call

from django.contrib import admin
from django.db import models
from .athlete_entry import AthleteEntryInline
from .team import Team
from .choices_constants import GENDER_CHOICES


class AthleteManager(models.Manager):
    '''Static classes related to athletes'''

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class Athlete(models.Model):
    '''Athlete info'''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    teams = models.ManyToManyField(Team)

    objects = AthleteManager()

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        return self.last_name + ", " + self.first_name


class AthleteAdmin(admin.ModelAdmin):
    '''Add inline edit for Athletes'''
    inlines = (AthleteEntryInline,)
