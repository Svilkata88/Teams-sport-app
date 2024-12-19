# Generated by Django 5.1.4 on 2024-12-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('playing', 'Playing'), ('finished', 'Finished'), ('postponed', 'Postponed')], default='scheduled', max_length=20),
        ),
    ]