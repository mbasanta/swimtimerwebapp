'''Classes related to Facility'''
from django.db import models
from localflavor.us.models import USStateField
from swimapp.models.course_code import CourseCode


class FacilityManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to facilities'''

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class Facility(models.Model):
    '''Facility info'''
    facility_name = models.CharField(max_length=45)
    elevation = models.IntegerField(blank=True, null=True)
    length_1 = models.ForeignKey(CourseCode,
                                 related_name='length_1_set',
                                 null=True)
    length_2 = models.ForeignKey(CourseCode,
                                 related_name='length_2_set',
                                 blank=True,
                                 null=True)
    lane_count = models.IntegerField(blank=True, null=True)
    addr_name = models.CharField(max_length=30, blank=True, null=True)
    addr = models.CharField(max_length=30, blank=True, null=True)
    addr_city = models.CharField(max_length=30, blank=True, null=True)
    addr_state = USStateField(blank=True, null=True)
    addr_zip = models.CharField(max_length=10, blank=True, null=True)
    addr_country = models.CharField(max_length=3, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = FacilityManager()  # pylint: disable=E1120

    class Meta:  # pylint: disable=W0232,C1001,R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.facility_name
