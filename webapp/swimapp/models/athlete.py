'''Classes related to Team'''
from django.contrib import admin
from django.db import models
from .athlete_entry import AthleteEntryInline


class AthleteManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to athletes'''

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class Athlete(models.Model):
    '''Athlete info'''
    # pylint: disable=C0330
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = AthleteManager()  # pylint: disable=E1120

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        return self.last_name + ", " + self.first_name


class AthleteAdmin(admin.ModelAdmin):  # pylint: disable=R0904
    '''Add inline edit for Athletes'''
    inlines = (AthleteEntryInline,)
