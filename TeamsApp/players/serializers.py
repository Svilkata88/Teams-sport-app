from rest_framework import serializers
from players.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ['password', 'last_login', 'date_joined', 'groups', 'user_permissions']
