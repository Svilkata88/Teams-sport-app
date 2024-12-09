from django.contrib import admin
from .models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['username', 'tel', 'team', 'is_staff', 'is_active', 'image']
    list_filter = ['team', 'is_staff', 'is_active']
    search_fields = ['username', 'team']
    ordering = ['username']