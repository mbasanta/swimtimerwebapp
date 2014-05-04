'''Classes related to stroke'''
from django.db import models


class Stroke(models.Model):
    '''Stroke used for the domain in Event object'''
    type_abbr = models.CharField(max_length=1)
    type_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.type_name
