from django import forms
from teams.models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ['rank', 'date_added', 'wins', 'draws', 'loses']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-2',
                'placeholder': 'Enter team name *'
            }),
            'logo': forms.FileInput(attrs={
                'class': 'w-full px-2 text-white rounded-lg',
                'placeholder': ''
            }),
            'date_founded': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Select a date',
                'class': 'px-2'
            }),
            'history': forms.Textarea(attrs={
                'class': 'w-full px-2 h-24',
                'placeholder': 'Enter your team history if you have one... '
            }),
            'administrators': forms.SelectMultiple(attrs={
                'class': 'w-full px-2',
            }),
        }