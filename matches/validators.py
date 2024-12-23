from datetime import datetime
from django.core.exceptions import ValidationError


current_datetime = datetime.now()


class TimeValidator:
    def __call__(self, value):
        if value < current_datetime.time():
            raise ValidationError('The game time must be later than the current time today.')

        return value


class DateValidator:
    def __call__(self, value):
        if value < current_datetime.date():
            raise ValidationError('The game time cannot be in the past.')

        return value
