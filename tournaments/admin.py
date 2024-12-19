from django.contrib import admin
from tournaments.models import Tournament


@admin.register(Tournament)
class AdminTournament(admin.ModelAdmin):
    list_display = ['name', 'number_of_participants', 'created_at', 'status', 'winner']
    list_filter = ['name', 'status', 'winner']
    search_fields = ['name']
    readonly_fields = ['created_at']

