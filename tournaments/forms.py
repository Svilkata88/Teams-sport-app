from django import forms
from django.core.exceptions import ValidationError

from tournaments.models import Tournament


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = [
            'name',
            'teams',
            'number_of_participants',
            'first_rating_points',
            'second_rating_points',
            'third_rating_points'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Tournament name'
            }),
            'teams': forms.SelectMultiple(attrs={
            }),
            'number_of_participants': forms.NumberInput(attrs={
                'placeholder': 'Max teams number'
            }),
            'first_rating_points': forms.NumberInput(attrs={
                'placeholder': 'First place points'
            }),
            'second_rating_points': forms.NumberInput(attrs={
                'placeholder': 'Second place points'
            }),
            'third_rating_points': forms.NumberInput(attrs={
                'placeholder': 'Third place points'
            }),
        }

    def clean(self):
        n_participants = self.cleaned_data.get('number_of_participants')
        teams = self.cleaned_data.get('teams')

        if len(teams) > n_participants:
            self.add_error(
                'number_of_participants',
                f'Max teams number must be greater than or equal to the number of selected teams ({len(teams)}).'
            )

        if len(teams) < 2:
            self.add_error(
                'teams',
                'You must select at least 2 teams.'
            )

        return self.cleaned_data
