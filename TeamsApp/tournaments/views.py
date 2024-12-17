from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from tournaments.forms import TournamentForm
from tournaments.models import Tournament


class DashboardTournaments(ListView):
    model = Tournament
    template_name = 'tournaments/dashboard-tournament.html'
    context_object_name = 'tournaments'

    def get_queryset(self):
        queryset = Tournament.objects.all().order_by('-created_at')
        return queryset


class CreateTournament(CreateView):
    model = Tournament
    form_class = TournamentForm
    template_name = 'tournaments/create-tournament.html'
    success_url = reverse_lazy('tournament-dashboard')

    # check if player is logged in and if he is in the group allowing tournament creation!
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'No permission to create a tournament. First you need to be logged in!')
            return redirect('tournament-dashboard')

        if not (request.user.groups.filter(name="Tournament Staff").exists() or request.user.is_superuser):
            messages.error(request, 'No permission to create a tournament. Need to be staff or admin!')
            return redirect('tournament-dashboard')

        return super().dispatch(request, *args, **kwargs)