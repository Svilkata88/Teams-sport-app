# Generated by Django 5.1.2 on 2024-12-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, default='team_profile_images/default_team.jpg', null=True, upload_to='team_profile_images/'),
        ),
    ]