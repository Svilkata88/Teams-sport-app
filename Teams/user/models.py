from django.contrib.auth.models import User
from django.db import models
from core import settings


# Create your models here.
class Player(User):
    tel = models.CharField(max_length=15)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='players')
    image = models.ImageField(upload_to='profile_images', null=True, blank=True, default='profile_images/default_profile.png')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

class Team(models.Model):
    name = models.CharField(max_length=150)
    rank = models.SmallIntegerField(default=0, blank=True)
    logo = models.ImageField(upload_to='profile_images', blank=True, null=True, default='profile_images/default_team.jpg')
    date_added = models.DateField(auto_now_add=True)
    date_founded = models.DateField(blank=True, null=True)
    history = models.TextField(null=True, blank=True)
    administrators = models.ManyToManyField('Player', related_name='administered_team')
    wins = models.SmallIntegerField(default=0)
    draws = models.SmallIntegerField(default=0)
    loses = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name
