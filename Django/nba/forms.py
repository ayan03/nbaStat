from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Player, Team
# Create your forms here.

class playerForm(ModelForm):
	class Meta:
		model = Player
		fields = ['name', 'pos', 'age', 'height', 'weight', 'team', 'points', 'assists', 'ofreb', 'defreb', 'steals']

class teamForm(ModelForm):
	class Meta:
		model = Team
		fields = ['name']
