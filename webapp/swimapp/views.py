"""Views for the swimapp"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Team
from .forms import TeamForm


@login_required
def edit_team(request, pk=None):
    """View to show for new or editing a team"""
    if request.method == "POST":
        team = Team(addr_country="USA")
        form = TeamForm(data=request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect("account_home")
    else:
        if pk is None:
            team = None
            form = TeamForm()
        else:
            team = get_object_or_404(Team, pk=pk)
            form = TeamForm(instance=team)
    return render(request, "swimapp/edit_team.html", {"form": form,
                                                      "team": team})


@login_required
def view_team(request, pk):
    """View to show for a readonly view of a team"""
    team = get_object_or_404(Team, pk=pk)
    if not team.users.filter(username=request.user.username):
        raise PermissionDenied
    return render(request, "swimapp/view_team.html", {"team": team})
