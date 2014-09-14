"""Team views for the swimapp"""
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from swimapp.models import Team
from swimapp.forms.team import TeamForm
# pylint: disable=E1123
#   Unexpected constructor argument
# pylint: disable=E1120
#   No argument X in constructor
# pylint: disable=E1101
#   Instace of X has no memeber X
# pylint: disable=C0103
#   Invalid argument name X


class TeamList(ListView):
    model = Team
    template_name = "swimapp/team_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TeamList, self).dispatch(*args, **kwargs)


class TeamView(DetailView):
    model = Team
    template_name = "swimapp/team_view.html"


class TeamCreate(CreateView):
    model = Team
    template_name = "swimapp/team_edit.html"
    form_class = TeamForm
    success_url = reverse_lazy('swimapp_team_list')

    def form_valid(self, form):
        form.instance.addr_country = 'USA'
        return super(TeamCreate, self).form_valid(form)


class TeamUpdate(UpdateView):
    model = Team
    template_name = "swimapp/team_edit.html"
    form_class = TeamForm
    success_url = reverse_lazy('swimapp_team_list')
