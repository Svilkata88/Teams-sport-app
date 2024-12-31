from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.players_dashboard, name='players-dashboard'),
    path('login/', include([
            path('', views.player_login, name='login'),
            path('reset-password', views.reset_password, name='reset-password'),
            path('reset-password-confirmation', views.reset_password_confirmation, name='reset-password-confirmation'),
         ])),
    path('logout/', views.player_logout, name='logout-page'), # да се оправи името / logout-page
    path('register/', views.player_register, name='register_player'),
    path('details/<int:pk>', views.player_details, name='details-page'), # да се оправи името / details-page
    path('update-player/<int:pk>', views.player_update, name='update-player'),
    path('update-player/<int:pk>/password-change', views.player_update_password, name='update-player-password'),
    path('delete/<int:pk>', views.player_delete, name='delete-player'),
    path('update-image/<int:pk>', views.player_update_image, name='update-player-image'),
    path('rest/', views.rest_players_all, name='rest-players-all')
]