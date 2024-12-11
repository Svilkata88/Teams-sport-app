from django.urls import path
from . import views

urlpatterns = [
    path('home', views.MatchesDashboard.as_view(), name='matches-dashboard'),
    path('create/', views.CreateMatch.as_view(), name='create-match'),
    path('detail/<int:pk>', views.DetailMatch.as_view(), name='match-detail'),
    path('delete/<int:pk>', views.DeleteMatch.as_view(), name='match-delete'),
]