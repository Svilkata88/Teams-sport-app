from django.db import models
from players.models import Player
from teams.models import Team


class Referee(models.Model):
    name = models.CharField(max_length=50)
    matches_count = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Playground(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Matches(models.Model):
    class StatusChoices(models.TextChoices):
        SCHEDULED = 'scheduled', 'Scheduled'
        PLAYING = 'playing', 'Playing'
        FINISHED = 'finished', 'Finished'
        POSTPONED = 'postponed', 'Postponed'

    home_team = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name='home_games')
    home_team_score = models.SmallIntegerField(default=0)

    away_team = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name='away_games')
    away_team_score = models.SmallIntegerField(default=0)

    referee = models.ForeignKey(to='matches.Referee', on_delete=models.CASCADE, related_name='matches', null=True, blank=True)
    status = models.CharField(choices=StatusChoices.choices, default=StatusChoices.SCHEDULED)
    playground = models.ForeignKey(to='matches.Playground', on_delete=models.CASCADE, related_name='pitch_matches')
    date_added = models.DateField(auto_now_add=True, editable=False)
    date = models.DateField()
    time = models.TimeField()
    creator = models.ForeignKey(to=Player, null=True, on_delete=models.SET_NULL, related_name='created_matches')

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} | status: {self.status}'
    
    class Meta:
        ordering = ['-pk'] 



