from rest_framework import serializers
from matches.models import Matches


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'

