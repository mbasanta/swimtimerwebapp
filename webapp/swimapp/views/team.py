'''Team views for the swimapp'''
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from swimapp.models import Team
from swimapp.forms.team import TeamForm
# pylint: disable=R0901
#   Too many acessestors
# pylint: disable=R0904
#   Too many public methods


class TeamList(ListView):
    '''List teams view'''
    model = Team
    template_name = 'swimapp/team_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TeamList, self).dispatch(*args, **kwargs)


class TeamView(DetailView):
    '''Team view'''
    model = Team
    template_name = 'swimapp/team_view.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TeamView, self).dispatch(*args, **kwargs)


class TeamCreate(CreateView):
    '''Team create view'''
    model = Team
    template_name = 'swimapp/team_edit.html'
    form_class = TeamForm
    success_url = reverse_lazy('swimapp_team_list')

    def form_valid(self, form):
        form.instance.addr_country = 'USA'
        return super(TeamCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TeamCreate, self).dispatch(*args, **kwargs)


class TeamUpdate(UpdateView):
    '''Team update view'''
    model = Team
    template_name = 'swimapp/team_edit.html'
    form_class = TeamForm
    success_url = reverse_lazy('swimapp_team_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TeamUpdate, self).dispatch(*args, **kwargs)
