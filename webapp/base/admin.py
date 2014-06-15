'''Add model classes to Admin site'''
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import AppUser
from .forms import AppUserAdmin


# Now register the new UserAdmin...
admin.site.register(AppUser, AppUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
