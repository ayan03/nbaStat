# Generated by Django 2.0.4 on 2018-07-05 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0003_auto_20180705_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100), max_length=100, unique=True),
        ),
    ]
