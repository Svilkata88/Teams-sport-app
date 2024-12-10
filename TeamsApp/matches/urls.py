from django.urls import path
from . import views

urlpatterns = [
    path('home', views.MatchesDashboard.as_view(), name='matches-dashboard'),
    path('create/', views.CreateMatch.as_view(), name='create-match')
]