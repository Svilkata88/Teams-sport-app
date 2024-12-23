from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from matches.forms import MatchCreateForm
from matches.models import Matches
from django.http import HttpResponseRedirect
from django.contrib import messages
from matches.serializers import MatchSerializer
from tournaments.models import Tournament


class MatchesDashboard(ListView):
    model = Matches
    context_object_name = 'matches'
    paginate_by = 10

    def get_template_names(self):
        if not self.request.user.is_authenticated:
            return ['common/index.html']
        return ['matches/matches-dashboard.html']

    def get_queryset(self):
        queryset = Matches.objects.all().order_by('-date_added')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        page = self.request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        matches = paginator.get_page(page)

        context['matches'] = matches
        return context


class CreateMatch(CreateView):
    model = Matches
    form_class = MatchCreateForm
    template_name = 'matches/matches-create.html'
    success_url = reverse_lazy('matches-dashboard')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        if form.instance.away_team == form.instance.home_team:
            messages.success(self.request, f"Away team must be different from the home team!")
            return render(self.request, 'matches/matches-create.html', self.get_context_data())
        return super().form_valid(form)


class DetailMatch(DetailView):
    template_name = 'matches/match-detail.html'
    context_object_name = 'match'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Matches.objects.get(pk=pk)

    def get_queryset(self):
        return Matches.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        match = self.get_object()
        creator = match.creator == self.request.user
        context['creator'] = creator
        return context


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
    fields = ['home_team', 'away_team', 'referee', 'status', 'playground', 'date', 'time', 'home_team_score',
              'away_team_score']
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


class RestMatches(ListAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchSerializer
    http_method_names = ['get']
