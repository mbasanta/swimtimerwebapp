'''Classes related to Lane Assignment in a heat'''
from django.db import models
from .heat import Heat


class LaneAssignment(models.Model):
    '''Lane Assignment info'''
    lane_number = models.IntegerField()
    swimmer_name = models.CharField(max_length=30)
    uss_num = models.CharField(max_length=14,
                               verbose_name='USA Swimming ID',
                               blank=True)
    heat = models.ForeignKey(Heat, related_name='lane_assignments')
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    class Meta(object):
        '''Meta for model to be used by django'''
        # pylint: disable=R0903
        app_label = 'swimapp'

    def __unicode__(self):
        return (self.heat.event.event_name + ", Heat " +
                str(self.heat.heat_number) + ", Lane " +
                str(self.lane_number))
