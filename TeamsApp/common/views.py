from django.shortcuts import render
from teams.models import Team


def index(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'common/index.html', context)
