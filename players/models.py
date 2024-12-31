from django.contrib.auth.models import AbstractUser
from django.db import models


class Player(AbstractUser):
    tel = models.CharField(max_length=15)
    team = models.ForeignKey(to='teams.Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='players')
    image = models.ImageField(upload_to='player_profile_images/', null=True, blank=True,
                              default='player_profile_images/default_profile.png')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'






