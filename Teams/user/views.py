from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from user.models import Team, Player
from .forms import RegisterPlayerForm, LoginPlayerForm, UpdatePlayerImageForm, UpdatePlayerForm, TeamForm, \
    PlayerSearchForm
from django.conf import settings


# Create your views here.
def index(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'teams/index.html', context)


def login_page(request):
    form = LoginPlayerForm(request.POST or None)
    next_url = request.GET.get('next')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"You've been logged in!!! Welcome {username}")
            return redirect(next_url if next_url else 'index')
        else:
            form.add_error(None, "Invalid username or password.")

    context = {
        'form': form,
        'next': next_url,
    }
    return render(request, 'user/login-page.html', context)


def logout_page(request):
    logout(request)
    return redirect('index')


def register_player_page(request):
    form = RegisterPlayerForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            player = form.save(commit=False)
            player.set_password(form.cleaned_data['password'])
            player.save()

            user = authenticate(username=player.username, password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {user.username}. You successfully registered!!!')
                return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'user/register-player.html', context)


def details_page(request, pk):
    player = Player.objects.get(pk=pk)
    form = UpdatePlayerImageForm()
    context = {
        'player': player,
        'form': form,
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, 'user/details-page.html', context)


def delete_player(request, pk):
    player = Player.objects.get(pk=pk)
    player.delete()
    messages.success(request, f'User {player.username} have been deleted!')
    return redirect('index')


def update_player_image(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = UpdatePlayerImageForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('details-page', kwargs={'pk': player.pk}))
    else:
        form = UpdatePlayerImageForm(instance=player)

    return render(request, 'user/details-page.html', {'form': form})


def update_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = UpdatePlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('details-page', kwargs={'pk': player.pk}))
    else:
        form = UpdatePlayerForm(instance=player)

    return render(request, 'user/update-player.html', {'form': form, 'player': player})


def teams_dashboard(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'teams/teams-dashboard.html', context)


def teams_detail_page(request, pk):
    team = Team.objects.get(pk=pk)
    context = {
        'team': team,
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
        if form.is_valid():
            team = form.save()
            team.administrators.add(request.user.player)
            # must be an instance of Player model not of User model
            administrators = form.cleaned_data['administrators']
            if administrators:
                team.administrators.add(*administrators)
            form = TeamForm()
            context = {
                'create_team_form': form,
                'new_team': team,
            }
            return redirect(reverse_lazy('teams-dashboard'))
    context = {
        'create_team_form': form,
    }
    return render(request, 'teams/create_team.html', context)


@login_required
def update_team(request, pk):
    team = Team.objects.get(pk=pk)
    form = TeamForm(request.POST or None, instance=team)
    if request.method == 'POST':
        form = TeamForm(request.POST or None, request.FILES, instance=team)
        if form.is_valid():
            team = form.save()
            team.administrators.add(request.user.player)
            administrators = form.cleaned_data['administrators']
            if administrators:
                team.administrators.add(*administrators)

            return redirect(reverse_lazy('teams-dashboard'))
    context = {
        'update_team_form': form,
        'team': team
    }
    return render(request, 'teams/update-team.html', context)


def players_dashboard(request):
    players = Player.objects.all()
    search_form = PlayerSearchForm(request.GET)

    if search_form.is_valid():
        search_input = search_form.cleaned_data['username']
        players = players.filter(username__icontains=search_input)

    context = {
        'players': players,
        'search_form': search_form,
    }

    return render(request, 'players/players-dashboard.html', context)
