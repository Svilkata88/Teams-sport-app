from random import randint
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import LoginPlayerForm, RegisterPlayerForm, UpdatePlayerImageForm, UpdatePlayerForm, PlayerSearchForm, \
    ResetPasswordForm, ConfirmationResetPassword, ChangePasswordForm
from players.models import Player
from django.conf import settings
from django.http import Http404

from .serializers import PlayerSerializer


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
            return redirect(next_url if next_url else 'matches-dashboard')
        else:
            form.add_error(None, "Invalid username or password.")

    context = {
        'form': form,
        'next': next_url,
    }
    return render(request, 'players/login-page.html', context)


def reset_password(request):
    # logit to be applied
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            messages.success(request, f"A 6-digit verification code was sent to {form.cleaned_data['tel']}!")
            return redirect(reverse_lazy('reset-password-confirmation'))
        else:
            return render(request, 'players/reset-password-player.html', {'form': form})

    context = {
        'form': ResetPasswordForm()
    }
    return render(request, 'players/reset-password-player.html', context)


def reset_password_confirmation(request):
    if request.method == 'POST':
        form = ConfirmationResetPassword(request.POST)
        if form.is_valid():
            random_code = randint(100000, 999999)  # random 6 digit code
            # logic for sending an SMS with a code for verification
            # ako кода изпратен на посоченият телефон е еднакъв с този написан тук формата минава и изпраща мейл на посочената поща
            # когато се отвори пощата трябва да има линк, на който се отваря вю, където потребителят въвежда новата си парола
        else:
            return render(request, 'players/reset-password-confirmation-player.html', {'form': form})

    context = {
        'form': ConfirmationResetPassword()
    }
    return render(request, 'players/reset-password-confirmation-player.html', context)


def player_logout(request):
    logout(request)
    return redirect('matches-dashboard')


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
                return redirect('matches-dashboard')

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
    try:
        player = Player.objects.get(pk=pk)
        player.delete()
        messages.success(request, f'User {player.username} have been deleted!')
        return redirect('matches-dashboard')
    except Player.DoesNotExist:
        raise Http404("Player not found")


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
        for field, errors in form.errors.items():
            for error in errors:
                messages.success(request, f"{field}: {error}")
    else:
        form = UpdatePlayerForm(instance=player)

    return render(request, 'players/update-player.html', {'form': form, 'player': player})


def player_update_password(request, pk):
    player = get_object_or_404(Player, pk=pk)

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        print(form.is_valid())
        if form.is_valid():
            form.save(player)
            messages.success(request, "Password updated successfully!")
            return redirect(reverse_lazy('login'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = ChangePasswordForm()

    return render(request, 'players/update-player-password.html', {'form': form, 'player': player})


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


@api_view(['GET'])
def rest_players_all(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
