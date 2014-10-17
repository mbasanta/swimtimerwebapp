'''Add model classes to Admin site'''
from django.contrib import admin
from swimapp.models.team import Team
from swimapp.models.team_registration import TeamRegistration
from swimapp.models.team_type import TeamType
from swimapp.models.meet import Meet, MeetAdmin
from swimapp.models.meet_type import MeetType
from swimapp.models.course_code import CourseCode
from swimapp.models.stroke import Stroke
from swimapp.models.event import Event, EventAdmin
from swimapp.models.meet_event import MeetEvent
from swimapp.models.meet_config import MeetConfig
from swimapp.models.version import Version
from swimapp.models.athlete import Athlete, AthleteAdmin
from swimapp.models.entry import Entry, EntryAdmin
from swimapp.models.athlete_entry import AthleteEntry, AthleteEntryAdmin
from swimapp.models.facility import Facility
from swimapp.models.fileupload import FileUpload


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
admin.site.register(FileUpload)
