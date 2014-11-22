'''Form for team display'''
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from swimapp.models.fileupload import FileUpload
# pylint: disable=R0903
#   Too few public methods
# pylint: disable=C1001
#   Old style class
# pylint: disable=W0232
#   No __init__ method


class FileUploadForm(ModelForm):
    '''Form for upload file display'''

    def __init__(self, *args, **kwargs):
        '''Team Form Constructor'''
        super(FileUploadForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'team_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-6'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Upload'))

        self.ajax_helper = self.helper
        self.helper.form_action = 'swimapp_file_upload_new'

    class Meta:
        '''Django meta info'''
        model = FileUpload
        exclude = ('status', 'processing_description',
                   'time_start_processing', 'time_end_processing')
