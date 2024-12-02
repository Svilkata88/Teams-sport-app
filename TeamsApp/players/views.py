from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import LoginPlayerForm, RegisterPlayerForm, UpdatePlayerImageForm, UpdatePlayerForm, PlayerSearchForm
from players.models import Player
from django.conf import settings


def player_login(request):
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
    return render(request, 'players/login-page.html', context)


def player_logout(request):
    logout(request)
    return redirect('index')


def player_register(request):
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
    return render(request, 'players/register-player.html', context)


def player_details(request, pk):
    player = Player.objects.get(pk=pk)
    form = UpdatePlayerImageForm()
    context = {
        'player': player,
        'form': form,
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, 'players/details-page.html', context)


def player_delete(request, pk):
    player = Player.objects.get(pk=pk)
    player.delete()
    messages.success(request, f'User {player.username} have been deleted!')
    return redirect('index')


def player_update_image(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = UpdatePlayerImageForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('details-page', kwargs={'pk': player.pk}))
    else:
        form = UpdatePlayerImageForm(instance=player)

    return render(request, 'players/details-page.html', {'form': form})


def player_update(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = UpdatePlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('details-page', kwargs={'pk': player.pk}))
    else:
        form = UpdatePlayerForm(instance=player)

    return render(request, 'players/update-player.html', {'form': form, 'player': player})


def players_dashboard(request):
    players = Player.objects.all()
    search_form = PlayerSearchForm(request.GET)

    if search_form.is_valid():
        search_input = search_form.cleaned_data['username']
        players = players.filter(username__icontains=search_input).order_by('username')

    context = {
        'players': players,
        'search_form': search_form,
    }

    return render(request, 'players/players-dashboard.html', context)
