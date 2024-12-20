# Generated by Django 5.1.4 on 2024-12-17 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0003_alter_team_administrators'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number_of_participants', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_rating_points', models.SmallIntegerField(default=0)),
                ('second_rating_points', models.SmallIntegerField(default=0)),
                ('third_rating_points', models.SmallIntegerField(default=0)),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('playing', 'Playing'), ('finished', 'Finished'), ('postponed', 'Postponed')], max_length=20)),
                ('second_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournaments_second', to='teams.team')),
                ('teams', models.ManyToManyField(related_name='tournaments', to='teams.team')),
                ('third_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournaments_third', to='teams.team')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournaments_won', to='teams.team')),
            ],
        ),
    ]
