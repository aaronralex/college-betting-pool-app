# Generated by Django 2.1.2 on 2018-10-31 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegebettingpoolapp', '0005_auto_20181030_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting', models.CharField(max_length=500, unique=True)),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='bettingsheet',
            name='game',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='betting_sheet',
        ),
        migrations.DeleteModel(
            name='BettingSheet',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]
