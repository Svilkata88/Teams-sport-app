from django.contrib import admin
from user.models import Player, Team
from unfold.admin import ModelAdmin


# Register your models here.
@admin.register(Player)
class PlayerAdmin(ModelAdmin):
   list_display = ['username', 'first_name', 'last_name', 'tel', 'team', 'password']


@admin.register(Team)
class TeamAdmin(ModelAdmin):
    pass

