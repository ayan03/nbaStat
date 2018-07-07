from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django import template
from django.shortcuts import render_to_response
from django.conf import settings
from .models import Player, Team

# Create your views here.
def index(request):
	return HttpResponse("hello try 2 world")

# Shows all players:
def player_list(request):
    players = Player.objects.all()
    return render(request, 'nba/player_list.html', {'players': players})

# Shows a player's individual stats
def player_detail(request, pk):    
    player = Player.objects.get(pk=pk)
    return render(request, 'nba/player_detail.html', {'player': player})


#lists players by team
def player_by_team(request, team_slug):
    teams = Team.objects.filter(name=team_slug)
    team = teams[0]
    players = Player.objects.all().filter(team__name=team_slug)
    context = {
        'team': team,
        'players': players
    }
    return render(request, 'nba/player_by_team.html', context)
