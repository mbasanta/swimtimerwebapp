'''Dashboard views for the swimapp'''
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic import TemplateView
from swimapp.forms.fileupload import FileUploadForm
from swimapp.models.choices_constants import 
from swimapp.models.fileupload import FileUpload
from swimapp.tasks import process_hy3_upload


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


class FileUploadList(ListView):
    '''List file upload view'''
    model = FileUpload
    template_name = 'swimapp/file_upload_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FileUploadList, self).dispatch(*args, **kwargs)


class FileUploadCreate(CreateView):
    '''File upload create view'''
    model = FileUpload
    template_name = 'swimapp/file_upload_edit.html'
    form_class = FileUploadForm
    success_url = reverse_lazy('swimapp_file_upload_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FileUploadCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save()
        if (self.filetype == FileUpload.HY3_FILE):
            process_hy3_upload.delay(self.object.id)
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FileUploadUpdate(UpdateView):
    '''File upload update view'''
    model = FileUpload
    template_name = 'swimapp/file_upload_edit.html'
    form_class = FileUploadForm
    success_url = reverse_lazy('swimapp_file_upload_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FileUploadUpdate, self).dispatch(*args, **kwargs)
