from django.urls import path
from . import views


urlpatterns = [
    path('', views.DashboardTournaments.as_view(), name='tournament-dashboard'),
    path('create/', views.CreateTournament.as_view(), name='tournament-create'),
    path('<str:status>', views.FilteredTournamentsMatchesDashboard.as_view(), name='f-matches-dashboard'),
]