# Generated by Django 5.1.2 on 2024-11-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_team_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='rank',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
    ]
