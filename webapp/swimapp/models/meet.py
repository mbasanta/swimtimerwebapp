'''Classes related to Meet'''
from django.db import models
from .meet_type import MeetType
from .course_code import CourseCode


class Meet(models.Model):
    '''Meet info'''
    meet_name = models.CharField(max_length=45)
    facility = models.CharField(max_length=45)
    start_date = models.DateField()
    end_date = models.DateField()
    age_up_date = models.DateField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    meet_type_1 = models.ForeignKey(MeetType,
                                    related_name='meet_type_1_set')
    meet_type_2 = models.ForeignKey(MeetType,
                                    related_name='meet_type_2_set')
    course_code_1 = models.ForeignKey(CourseCode,
                                      related_name='course_code_1_set')
    course_code_2 = models.ForeignKey(CourseCode,
                                      related_name='course_code_2_set')
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.meet_name
