from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from matches.forms import MatchCreateForm
from matches.models import Matches
from django.http import HttpResponseRedirect
from django.contrib import messages


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


class CreateMatch(CreateView):
    model = Matches
    form_class = MatchCreateForm
    template_name = 'matches/matches-create.html'
    success_url = reverse_lazy('matches-dashboard')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DetailMatch(DetailView):
    
    template_name = 'matches/match-detail.html'
    context_object_name = 'match' 

    def get_object(self):
        pk = self.kwargs.get('pk')  
        return Matches.objects.get(pk=pk)
    
    def get_queryset(self):
        return Matches.objects.all()
    

class DeleteMatch(DeleteView):
    model = Matches
    template_name = 'matches/match-detail.html'
    success_url = reverse_lazy('matches-dashboard')
  
    def dispatch(self, request, *args, **kwargs):
        match = self.get_object()
        if match.creator != request.user:
            messages.error(request, "You are not authorized to delete this match.")
            return HttpResponseRedirect(reverse_lazy('matches-dashboard'))
        return super().dispatch(request, *args, **kwargs)


class UpdateMatch(UpdateView):
    model = Matches
    fields = ['home_team', 'away_team', 'referee', 'status', 'playground', 'date', 'time']
    form = MatchCreateForm
    template_name = 'matches/matches-update.html'
    success_url = reverse_lazy('matches-dashboard')

    def dispatch(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            if obj.creator != self.request.user:
                raise PermissionError("You are not authorized to update this match.")
        except PermissionError as error:
            messages.error(request, str(error))
            return redirect('matches-dashboard')

        return super().dispatch(request, *args, **kwargs)
