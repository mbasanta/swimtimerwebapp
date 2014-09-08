"""Team views for the swimapp"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
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
    if request.user.is_admin or team.users.filter(email=request.user.email):
        return render(request, "swimapp/view_team.html", {"team": team})
    else:
        raise PermissionDenied
