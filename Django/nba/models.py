from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)

	def __str__(self):
		return self.name


class Player(models.Model):
	name = models.CharField(max_length=100)
	age = models.FloatField(max_length=3)
	team = models.ForeignKey(Team, models.SET_NULL, blank=True, null=True,)

	def __str__(self):
		return self.name

