'''Form for team display'''
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from swimapp.models import Team
# pylint: disable=C1001
#   old style class definition
# pylint: disable=W0232
#   No init method
# pylint: disable=R0903
#   Too few public methods


class TeamForm(ModelForm):
    '''Form for team display'''

    def __init__(self, *args, **kwargs):
        '''Team Form Constructor'''
        super(TeamForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'team_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-6'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        '''Django meta info'''
        model = Team
        exclude = ("addr_country", "fax")
