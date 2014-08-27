'''Classes related to Athlete Entry ManyToMany relationships'''
from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse


class AthleteEntryManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to athelete entries'''

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class AthleteEntry(models.Model):
    '''Athlete Entry info'''
    # Used the lazy reference method for the FK to avoid circular imports
    # http://stackoverflow.com/q/4379042/
    athlete = models.ForeignKey('swimapp.Athlete')
    entry = models.ForeignKey('swimapp.Entry')
    athlete_order = models.IntegerField(
        blank=True,
        null=True)

    objects = AthleteEntryManager()  # pylint: disable=E1120

    class Meta:  # pylint: disable=R0903,W0232,C1001
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return str(self.athlete) + ' : ' + str(self.entry)

    def get_absolute_url(self):  # pylint: disable=E0202
        '''Get reverse URL'''
        # pylint: disable=E1101
        return reverse('swimapp_view_athlete_event', args=[self.id])


class AthleteEntryInline(admin.TabularInline):  # pylint: disable=R0901
    '''Inline methods for meet events'''
    model = AthleteEntry
    extra = 1


class AthleteEntryAdmin(admin.ModelAdmin):
    """
    Override AthleteEntryAdmin to eliminate some of the
    excessive queries
    """

    def queryset(self, request):
        """Override queryset to limit excessive queries"""
        return super(AthleteEntryAdmin, self).queryset(request) \
            .select_related('athlete', 'entry', 'entry__meetevent',
                            'entry__meetevent__event')
