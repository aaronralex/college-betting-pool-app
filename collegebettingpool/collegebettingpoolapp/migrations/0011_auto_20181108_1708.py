# Generated by Django 2.1.2 on 2018-11-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegebettingpoolapp', '0010_auto_20181108_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='bet_selection',
        ),
        migrations.AddField(
            model_name='bet',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]