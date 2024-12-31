from django import forms
from django.core.exceptions import ValidationError

from players.models import Player
from players.validators import PhoneNumberValidator, PhoneNumberExistsValidator
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
                'placeholder': 'Phone number * +349 --- --- ---',
            }),
            'password': forms.PasswordInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'Password *',
            }),
        }

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        validator = PhoneNumberValidator()
        try:
            validator(tel)
        except ValidationError as e:
            raise ValidationError(e.messages)

        return tel

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!!!")

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

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        validator = PhoneNumberValidator()
        try:
            validator(tel)
        except ValidationError as e:
            raise ValidationError(e.messages)

        return tel


class PlayerSearchForm(forms.Form):
    username = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
                'placeholder': 'Search player...',
                'class': 'pl-2 rounded-lg ml-7',
        }),
        label=''
    )


class ResetPasswordForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ['tel',]
        widgets = {
            'tel': forms.TextInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'Phone number * +349 --- --- ---',
            }),
        }

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        validator1 = PhoneNumberValidator()
        validator2 = PhoneNumberExistsValidator()
        try:
            validator1(tel)
            validator2(tel)
        except ValidationError as e:
            raise ValidationError(e.messages)

        return tel


class ConfirmationResetPassword(forms.ModelForm):
    code_field = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': FORM_CLASS_STYLES,
            'placeholder': '6 digit code --- ---',
        })
    )

    class Meta:
        model = Player
        fields = ['email', 'code_field']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': 'email@email.com',
                'required': 'required',
            }),
            'code_field': forms.NumberInput(attrs={
                'class': FORM_CLASS_STYLES,
                'placeholder': '6 digit code --- ---',
            }),
        }


class ChangePasswordForm(forms.Form):
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': FORM_CLASS_STYLES,
            'placeholder': 'Confirm new Password *',
        })
    )
    new_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': FORM_CLASS_STYLES,
            'placeholder': 'New Password *',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match!!!")

        return cleaned_data

    def save(self, player, commit=True):
        new_password = self.cleaned_data['new_password']
        player.set_password(new_password)

        if commit:
            player.save()
        return player

