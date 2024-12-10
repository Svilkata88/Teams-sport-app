from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.MatchesDashboard.as_view(), name='matches-dashboard')
]