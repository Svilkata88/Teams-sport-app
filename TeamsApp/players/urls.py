from django.urls import path
from . import views

urlpatterns = [
    path('', views.players_dashboard, name='players-dashboard'),
    path('login/', views.player_login, name='login'),
    path('logout/', views.player_logout, name='logout-page'), # да се оправи името / logout-page
    path('register/', views.player_register, name='register_player'),
    path('details/<int:pk>', views.player_details, name='details-page'), # да се оправи името / details-page
    path('update-player/<int:pk>', views.player_update, name='update-player'),
    path('delete/<int:pk>', views.player_delete, name='delete-player'),
    path('update-image/<int:pk>', views.player_update_image, name='update-player-image'),
]