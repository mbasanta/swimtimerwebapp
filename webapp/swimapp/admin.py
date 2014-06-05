'''Add model classes to Admin site'''
from django.contrib import admin
from .models import Team, TeamRegistration, TeamType
from .models import Meet, MeetType, CourseCode
from .models import Stroke, Event, Heat, LaneAssignment
from .models import MeetEvent
from .models import MeetAdmin, EventAdmin


admin.site.register(Team)
admin.site.register(TeamRegistration)
admin.site.register(TeamType)
admin.site.register(Meet, MeetAdmin)
admin.site.register(MeetType)
admin.site.register(CourseCode)
admin.site.register(Stroke)
admin.site.register(Event, EventAdmin)
admin.site.register(Heat)
admin.site.register(LaneAssignment)
admin.site.register(MeetEvent)
