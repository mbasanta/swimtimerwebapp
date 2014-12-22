'''Classes related to a DQ'''

# pylint: disable=C0103
# # Invalid variable name
# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=E1120
# # No value in constructor call

from django.db import models
from swimapp.models.judge import Judge
from swimapp.models.violation import Violation


class DQManager(models.Manager):
    '''Static classes related to dqs'''

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def get_queryset(self):
        '''Override manager to use select related'''
        return super(DQManager, self).get_queryset() \
            .select_related('entry')

    def create_from_serializer(self, dq_data, entry):
        '''get or create a dq from the serializer data'''
        judge = Judge.objects.create_from_serializer(dq_data['judge'])
        dq = self.create(
            reason=dq_data['reason'],
            entry=entry,
            judge=judge,)

        return dq


class DQ(models.Model):
    '''DQ info'''
    violation = models.ForeignKey(Violation)
    reason = models.CharField(max_length=500)
    entry = models.ForeignKey('swimapp.Entry')
    judge = models.ForeignKey(Judge)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = DQManager()

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        '''
        Define the __unicode__ method, which is used by related
        models by default.
        '''
        return unicode(self.reason)
