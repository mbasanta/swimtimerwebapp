'''Classes related to a false start'''

# pylint: disable=C0103
# # Invalid variable name
# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=E1120
# # No value in constructor call

from django.db import models
from swimapp.models.judge import Judge


class FalseStartManager(models.Manager):
    '''Static classes related to false start'''

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def get_queryset(self):
        '''Override manager to use select related'''
        return super(FalseStartManager, self).get_queryset() \
            .select_related('entry')

    def create_from_serializer(self, falsestart_data, entry):
        '''get or create a false start from the serializer data'''
        judge = Judge.objects.create_from_serializer(falsestart_data['judge'])
        falsestart = self.create(
            lane=falsestart_data['lane'],
            entry=entry,
            judge=judge,)

        return falsestart


class FalseStart(models.Model):
    '''false start info'''
    lane = models.IntegerField()
    entry = models.ForeignKey('swimapp.Entry')
    judge = models.ForeignKey(Judge)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = FalseStartManager()

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        '''
        Define the __unicode__ method, which is used by related
        models by default.
        '''
        return 'False Start - Lane ' + unicode(self.lane)
