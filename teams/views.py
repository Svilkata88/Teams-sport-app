from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from teams.forms import TeamForm
from teams.models import Team


def teams_dashboard(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'teams/teams-dashboard.html', context)


def team_details(request, pk):
    team = Team.objects.get(pk=pk)
    administrators = team.administrators.all()

    context = {
        'team': team,
        'administrators': administrators,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'teams/teams-details-page.html', context)


@login_required
def delete_team(request, pk):
    team = Team.objects.get(pk=pk)
    if request.method == 'POST':
        team.delete()
        messages.success(request, f'The team {team.name} has been deleted.')
        return redirect(reverse_lazy('teams-dashboard'))


@login_required
def create_team(request):
    form = TeamForm(request.POST or None)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            team = form.save()
            team.administrators.add(request.user)

            administrators = form.cleaned_data['administrators']
            if administrators:
                team.administrators.add(*administrators)
            return redirect(reverse_lazy('teams-dashboard'))

    context = {
        'create_team_form': form,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'teams/create_team.html', context)


@login_required
def update_team(request, pk):
    team = Team.objects.get(pk=pk)
    form = TeamForm(request.POST or None, instance=team)

    if request.method == 'POST':
        form = TeamForm(request.POST or None, request.FILES, instance=team)
        if form.is_valid():
            if request.user not in team.administrators.all():
                messages.error(request, "You are not allowed to perform this action!")
                return redirect(reverse_lazy('teams-dashboard'))
            team = form.save()
            team.administrators.add(request.user)
            administrators = form.cleaned_data['administrators']
            if administrators:
                team.administrators.add(*administrators)

            return redirect(reverse_lazy('teams-dashboard'))

    context = {
        'update_team_form': form,
        'team': team
    }

    return render(request, 'teams/update-team.html', context)
