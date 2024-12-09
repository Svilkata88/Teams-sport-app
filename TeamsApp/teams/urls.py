from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teams_dashboard, name='teams-dashboard'),
    path('create/', views.create_team, name='create-team'),
    path('<int:pk>/', include([
        path('', views.team_details, name='teams-details-page'),
        path('delete/', views.delete_team, name='delete-team'),
        path('update/', views.update_team, name='update-team'),
    ])),
]