
from django.urls import path
from django.urls import include
from .views import (login_page, details_page, register_player_page, logout_page, delete_player, update_player_image,
                    update_player,
                    teams_dashboard,
                    teams_detail_page,
                    delete_team,
                    create_team,
                    update_team,
                    players_dashboard,)

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_player_page, name='register_player'),
    path('logout/', logout_page, name='logout-page'),
    path('details/<int:pk>', details_page, name='details-page'),
    path('delete/<int:pk>', delete_player, name='delete-player'),
    path('update-player/<int:pk>', update_player, name='update-player'),
    path('update-image/<int:pk>', update_player_image, name='update-player-image'),
    path('teams/', teams_dashboard, name='teams-dashboard'),
    path('teams/<int:pk>', teams_detail_page, name='teams-details-page'),
    path('teams/create/', create_team, name='create-team'),
    path('teams/<int:pk>/', include([
            path('delete/', delete_team, name='delete-team'),
            path('update/', update_team, name='update-team'),
        ])),
    path('players/', players_dashboard, name='players-dashboard')
]