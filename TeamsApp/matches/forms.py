from django import forms
from matches.models import Matches


class MatchCreateForm(forms.ModelForm):
    class Meta:
        model = Matches
        fields = ['home_team', 'away_team', 'referee', 'status', 'playground', 'game_datetime']
        widges = {
            'home_team': forms.Select(),
            'away_team': forms.Select(),
            'referee': forms.Select(),
            'status': forms.Select(),
            'playground': forms.Select(),
            'game_datetime': forms.DateTimeInput(),
        }