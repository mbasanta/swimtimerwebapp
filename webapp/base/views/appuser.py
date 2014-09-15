'''App User views for the swimapp'''
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from base.models import AppUser
from base.forms import UserCreationForm, UserChangeForm
# pylint: disable=R0901
#   Too many acessestors
# pylint: disable=R0904
#   Too many public methods


class AppUserList(ListView):
    '''List app user view'''
    model = AppUser
    template_name = 'base/appuser_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppUserList, self).dispatch(*args, **kwargs)


class AppUserView(DetailView):
    '''app user view'''
    model = AppUser
    template_name = 'base/appuser_view.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppUserView, self).dispatch(*args, **kwargs)


class AppUserCreate(CreateView):
    '''AppUser create view'''
    model = AppUser
    template_name = 'base/appuser_edit.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('base_appuser_list')

    def form_valid(self, form):
        #form.instance.addr_country = 'USA'
        return super(AppUserCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppUserCreate, self).dispatch(*args, **kwargs)


class AppUserUpdate(UpdateView):
    '''AppUser update view'''
    model = AppUser
    template_name = 'base/appuser_edit.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('base_appuser_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppUserUpdate, self).dispatch(*args, **kwargs)
