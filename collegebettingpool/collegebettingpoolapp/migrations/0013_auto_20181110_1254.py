# Generated by Django 2.1.2 on 2018-11-10 18:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collegebettingpoolapp', '0012_gameofweekscores'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GameOfWeekScores',
            new_name='GameOfWeekScore',
        ),
    ]
