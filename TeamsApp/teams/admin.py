from django.contrib import admin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_players', 'rank', ]
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ['date_added', 'date_founded']

    def get_players(self, obj):
        return ', '.join(player.name for player in obj.players.all())

    get_players.short_description = 'players'
