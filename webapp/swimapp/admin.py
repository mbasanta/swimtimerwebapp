'''Add model classes to Admin site'''
from django.contrib import admin
from .models import Team, TeamRegistration, TeamType
from .models import Meet, MeetType, CourseCode
from .models import Stroke, Event
from .models import MeetEvent
from .models import MeetAdmin, EventAdmin
from .models import MeetConfig
from .models import Version
from .models import Athlete, AthleteAdmin
from .models import Entry, EntryAdmin
from .models import AthleteEntry, AthleteEntryAdmin
from .models import Facility


admin.site.register(Team)
admin.site.register(TeamRegistration)
admin.site.register(TeamType)
admin.site.register(Meet, MeetAdmin)
admin.site.register(MeetType)
admin.site.register(CourseCode)
admin.site.register(Stroke)
admin.site.register(Event, EventAdmin)
admin.site.register(MeetEvent)
admin.site.register(MeetConfig)
admin.site.register(Version)
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(AthleteEntry, AthleteEntryAdmin)
admin.site.register(Facility)
