from django.contrib import admin
from matches.models import Matches, Referee, Playground


@admin.register(Matches)
class MatchesAdmin(admin.ModelAdmin):
    list_display = ['home_team', 'away_team', 'referee', 'home_team_score', 'away_team_score', 'status', 'game_datetime', 'creator']
    list_filter = ['referee', 'status', 'creator']
    search_fields = ['home_team', 'away_team', 'status', 'referee', 'creator']

    fieldsets = (
        ('Match Details', {
            'fields': ('home_team', 'away_team', 'home_team_score', 'away_team_score', 'status', 'game_datetime')
        }),
        ('Additional Information', {
            'fields': ('referee', 'playground', 'creator')
        }),
    )


@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ['name', 'matches_count']
    search_fields = ['name']


@admin.register(Playground)
class PlaygroundAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name']