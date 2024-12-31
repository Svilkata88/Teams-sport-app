from django import forms
from django.core.exceptions import ValidationError
from matches.models import Matches


class MatchCreateForm(forms.ModelForm):
    # checking if the status field is set to finished and if yes it is disabled
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.status == Matches.StatusChoices.FINISHED:
            for field in self.fields:
                self.fields[field].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Matches
        fields = ['home_team', 'away_team', 'referee', 'status', 'playground', 'date', 'time', 'home_team_score',
                  'away_team_score']
        widgets = {
            'home_team': forms.Select(),
            'away_team': forms.Select(),
            'referee': forms.Select(),
            'status': forms.Select(),
            'playground': forms.Select(),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'home_team_score': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter home team score',
            }),
            'away_team_score': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter away team score',
            }),
        }



