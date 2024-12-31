from django.core.exceptions import ValidationError
from players.models import Player


class PhoneNumberValidator:
    def __call__(self, value):
        if not value.startswith('+359') or len(value) != 13:
            raise ValidationError("Must be like: +359 --- --- ---")


class PhoneNumberExistsValidator:
    def __call__(self, value):
        tel_numbers = Player.objects.values_list('tel', flat=True)
        if value not in tel_numbers:
            raise ValidationError("No such telephone number!")
