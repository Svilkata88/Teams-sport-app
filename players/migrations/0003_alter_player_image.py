# Generated by Django 5.1.2 on 2024-12-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, default='player_profile_images/default_profile.png', null=True, upload_to='player_profile_images/'),
        ),
    ]