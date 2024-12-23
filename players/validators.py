from django.core.exceptions import ValidationError


class PhoneNumberValidator:
    def __call__(self, value):
        if not value.startswith('+359') or len(value) != 13:
            raise ValidationError("Must be like: +359 --- --- ---")
