from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=150)
    rank = models.SmallIntegerField(default=0, blank=True)
    logo = models.ImageField(upload_to='team_profile_images/', blank=True, null=True, default='team_profile_images/default_team.jpg')
    date_added = models.DateField(auto_now_add=True)
    date_founded = models.DateField(blank=True, null=True)
    history = models.TextField(null=True, blank=True)
    administrators = models.ManyToManyField(to='players.Player', related_name='administered_team')
    wins = models.SmallIntegerField(default=0)
    draws = models.SmallIntegerField(default=0)
    loses = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

