'''Classes related to meet types'''
from django.db import models


class MeetConfig(models.Model):
    '''Meet configurations used for the domain in Meet object'''
    type_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.type_name
