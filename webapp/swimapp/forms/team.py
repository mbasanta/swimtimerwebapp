'''Form for team display'''
from django.forms import ModelForm
from swimapp.models import Team
# pylint: disable=C1001
#   old style class definition
# pylint: disable=W0232
#   No init method
# pylint: disable=R0903
#   Too few public methods


class TeamForm(ModelForm):
    '''Form for team display'''
    class Meta:
        '''Django meta info'''
        model = Team
        exclude = ["addr_county"]
