# Generated by Django 2.0.4 on 2018-07-08 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0007_auto_20180705_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='ppg',
            field=models.FloatField(default=0, max_length=3),
        ),
    ]