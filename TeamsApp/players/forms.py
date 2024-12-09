from django import forms
from players.models import Player
from teams.models import Team

FORM_CLASS_STYLES = 'form-input text-black border-2 border-gray-300 rounded-md p-2 w-full rounded-xl'


class LoginPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'Enter your username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'Enter your password'
            }),
        }


class RegisterPlayerForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': FORM_CLASS_STYLES,
            'placeholder': 'Confirm Password *',
        })
    )

    class Meta:
        model = Player
        fields = ['username', 'first_name', 'last_name', 'tel', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'Enter your username *'
            }),
            'first_name': forms.TextInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'Last Name',
            }),
            'tel': forms.TextInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'Phone number *',
            }),
            'password': forms.PasswordInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'Password *',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class UpdatePlayerImageForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'placeholder': 'Upload your file',
                'class': 'rounded-lg text-sm'
            })
        }
        labels = {
            'image': ''
        }


class UpdatePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['username', 'tel', 'email', 'first_name', 'last_name', 'image', 'team']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'pl-2 rounded-lg'
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First name',
                'class': 'pl-2 rounded-lg'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last name',
                'class': 'pl-2 rounded-lg'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'pl-2 rounded-lg'
            }),
            'tel': forms.TextInput(attrs={
                'placeholder': 'Phone number',
                'class': 'pl-2 rounded-lg'
            }),
            'image': forms.FileInput(attrs={
                'accept': 'image/*',
                'class': 'text-white rounded-lg'
            }),
        }

    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        required=False,
        empty_label="Select a team",
        widget=forms.Select(attrs={
            'class': 'pl-2 rounded-lg'
        })
    )


class PlayerSearchForm(forms.Form):
    username = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
                'placeholder': 'Search player...',
                'class': 'pl-2 rounded-lg ml-7',
        }),
        label=''
    )