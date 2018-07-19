from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)

	def __str__(self):
		return self.name


class Player(models.Model):
	name = models.CharField(max_length=100)
	pos = models.CharField(max_length=5, default='null')
	age = models.FloatField(max_length=3)
	team = models.ForeignKey(Team, models.SET_NULL, blank=True, null=True,)
	points = models.FloatField(max_length=3, default=0)
	assists = models.FloatField(max_length=3, default=0)
	ofreb = models.FloatField(max_length=3, default=0)
	defreb = models.FloatField(max_length=3, default=0)
	steals = models.FloatField(max_length=3, default=0)


	def __str__(self):
		return self.name

