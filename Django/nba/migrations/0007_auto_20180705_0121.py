# Generated by Django 2.0.4 on 2018-07-05 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0006_auto_20180705_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
