'''Dashboard views for the swimapp'''
import random
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from swimapp.forms.fileupload import FileUploadForm
from swimapp.models.team import Team


class DashboardView(TemplateView):
    '''dashboard view'''
    template_name = 'swimapp/user_dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['random_number'] = random.randrange(1, 100)
        context['teams'] = Team.objects.filter(users=self.request.user) \
            .select_related('team_reg', 'team_type')
        context['upload_form'] = FileUploadForm
        return context
