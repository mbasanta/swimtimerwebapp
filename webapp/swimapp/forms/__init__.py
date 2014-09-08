from django.forms import ModelForm
from .models import Team


class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ["addr_county"]
