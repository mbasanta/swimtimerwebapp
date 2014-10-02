'''Dashboard views for the swimapp'''
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from swimapp.forms.fileupload import FileUploadForm
from swimapp.models.fileupload import FileUpload


class FileUploadView(TemplateView):
    '''file upload view'''

    model = FileUpload
    template_name = 'swimapp/file_upload.html'
    form_class = FileUploadForm
    #success_url = reverse_lazy('swimapp_team_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(FileUploadView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(FileUploadView, self).get_context_data(
            *args, **kwargs)
        context['form'] = FileUploadForm
        #context['teams'] = Team.objects.filter(users=self.request.user) \
            #.select_related('team_reg', 'team_type')
        return context
