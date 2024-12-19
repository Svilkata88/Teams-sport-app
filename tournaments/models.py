from django.db import models
from teams.models import Team


class Tournament(models.Model):
    class StatusChoices(models.TextChoices):
        SCHEDULED = 'scheduled', 'Scheduled'
        PLAYING = 'playing', 'Playing'
        FINISHED = 'finished', 'Finished'
        POSTPONED = 'postponed', 'Postponed'

    name = models.CharField(max_length=50)
    teams = models.ManyToManyField(to=Team, related_name='tournaments')
    number_of_participants = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    first_rating_points = models.SmallIntegerField(default=0)
    second_rating_points = models.SmallIntegerField(default=0)
    third_rating_points = models.SmallIntegerField(default=0)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.SCHEDULED)
    winner = models.ForeignKey(to=Team, blank=True, null=True, on_delete=models.SET_NULL, related_name='tournaments_won')
    second_place = models.ForeignKey(to=Team, blank=True, null=True, on_delete=models.SET_NULL, related_name='tournaments_second')
    third_place = models.ForeignKey(to=Team, blank=True, null=True, on_delete=models.SET_NULL, related_name='tournaments_third')

    def __str__(self):
        return self.name
