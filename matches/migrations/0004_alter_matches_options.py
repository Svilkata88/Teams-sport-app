# Generated by Django 5.1.4 on 2024-12-17 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_remove_matches_game_datetime_matches_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matches',
            options={'ordering': ['-pk']},
        ),
    ]
