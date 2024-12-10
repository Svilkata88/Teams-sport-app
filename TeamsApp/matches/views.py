from django.shortcuts import render
from django.views.generic import ListView
from matches.models import Matches


class MatchesDashboard(ListView):
    model = Matches
    context_object_name = 'matches'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['matches'] = Matches.objects.all()
        return context

    def get_template_names(self):
        if not self.request.user.is_authenticated:
            return ['common/index.html']
        return ['matches/matches-dashboard.html']