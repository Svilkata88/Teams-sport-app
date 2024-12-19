from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from TeamsApp import settings
from matches import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MatchesDashboard.as_view(), name='matches-dashboard'),
    path('players/', include('players.urls')),
    path('teams/', include('teams.urls')),
    path('matches/', include('matches.urls')),
    path('tournaments/', include('tournaments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL)
