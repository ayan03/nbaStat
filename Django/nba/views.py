from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django import template
from django.shortcuts import render_to_response
from django.conf import settings
from .models import Player, Team
from .forms import playerForm, teamForm

# Create your views here.
def home(request):
	return render(request, 'nba/home.html')

def search(request):
	error = False
	if 'team1' in request.GET:
		team1 = request.GET['team1']
		if not team1:
			error = True
		else:
			teams = Team.objects.values('name').distinct().filter(name=team1).distinct()
		if 'team2' in request.GET:
			team2 = request.GET['team2']
			if not team2:
				error = True
			else:
				teams2 = Team.objects.values('name').distinct().filter(name=team2)

				## finds advantages of the two teams
				p1 = Player.objects.filter(team__name=team1)
				p2 = Player.objects.filter(team__name=team2)
				adv1 = find_advantages(p1)
				weak1 = find_weaknesses(p1)
				adv2 = find_advantages(p2)
				weak2 = find_weaknesses(p2)

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			error = True
		else:
			players = Player.objects.filter(name=name)

			if 'name2' in request.GET:
				name2 = request.GET['name2']
				if not name2:
					error = True
				else:
					players2 = Player.objects.filter(name=name2)
					players = players|players2
			if players.count() > 0 and teams.count() > 0:
				return render(request, 'nba/search_results.html', {'player1': players[0], 'player2': players[1], 
							'query': name, 'team1': teams[0], 'team2': teams[1], 'adv1': adv1, 'weak1': weak1, 
							'adv2': adv2, 'weak2': weak2})
			error = True
			return render(request, 'nba/home.html', {'error': error})
	return render(request, 'nba/home.html', {'error': error})

# Shows all teams:
def team_list(request):
	teams = Team.objects.values('name').distinct().order_by('name')
	return render(request, 'nba/team_list.html', {'teams': teams})

# Shows all players:
def player_list(request):
    players = Player.objects.all()
    return render(request, 'nba/player_list.html', {'players': players})

# Shows all players by categories:
def player_list_cats(request, cat_slug):
	players = Player.objects.all().order_by('-' + cat_slug)
	return render(request, 'nba/player_list.html', {'players': players})

	# Shows all players by position:
def player_by_pos(request, pos_slug):
	pgs = Player.objects.all().filter(pos='PG')
	sgs = Player.objects.all().filter(pos='SG') 
	sfs = Player.objects.all().filter(pos='SF')
	pfs = Player.objects.all().filter(pos='PF')
	cs = Player.objects.all().filter(pos='C')
	gs = Player.objects.all().filter(pos='G')
	fs = Player.objects.all().filter(pos='F')
	fcs = Player.objects.all().filter(pos='FC')
	gfs = Player.objects.all().filter(pos='GF')
	if pos_slug == 'guard':
		ps = pgs|sgs|gs|gfs
	elif pos_slug == 'pg':
		ps = pgs|gs
	elif pos_slug == 'sg':
		ps = sgs|gs|gfs
	elif pos_slug == 'sf':
		ps = sfs|gfs|fs
	elif pos_slug == 'pf':
		ps = pfs|fcs|fs
	elif pos_slug == 'forward':
		ps = sfs|pfs|fs|fcs|gfs
	elif pos_slug == 'center':
		ps = cs|fcs
	players = ps
	context = {
		'pos': pos_slug,
		'players': players
	}
	return render(request, 'nba/player_by_pos.html', context)

#same as above but organize by category
def player_by_pos_cats(request, pos_slug, cat_slug):
	pgs = Player.objects.all().filter(pos='PG')
	sgs = Player.objects.all().filter(pos='SG') 
	sfs = Player.objects.all().filter(pos='SF')
	pfs = Player.objects.all().filter(pos='PF')
	cs = Player.objects.all().filter(pos='C')
	gs = Player.objects.all().filter(pos='G')
	fs = Player.objects.all().filter(pos='F')
	fcs = Player.objects.all().filter(pos='FC')
	gfs = Player.objects.all().filter(pos='GF')
	if pos_slug == 'guard':
		ps = pgs|sgs|gs|gfs
	elif pos_slug == 'pg':
		ps = pgs|gs
	elif pos_slug == 'sg':
		ps = sgs|gs|gfs
	elif pos_slug == 'sf':
		ps = sfs|gfs|fs
	elif pos_slug == 'pf':
		ps = pfs|fcs|fs
	elif pos_slug == 'forward':
		ps = sfs|pfs|fs|fcs|gfs
	elif pos_slug == 'center':
		ps = cs|fcs
	players = ps.order_by('-'+cat_slug)
	context = {
		'pos': pos_slug,
		'players': players
	}
	return render(request, 'nba/player_by_pos.html', context)


# Shows a player's individual stats
def player_detail(request, pk):    
    player = Player.objects.get(pk=pk)
    return render(request, 'nba/player_detail.html', {'player': player})


#lists players by team
#average weight: 238lb
#average height: 6-7 
#average age: 26.5 (young < 26.0) (old > 27.0)
#average points: 106.3
#average rebounds: 43.5
def player_by_team(request, team_slug):
    teams = Team.objects.filter(name=team_slug)
    team = teams[0]
    players = Player.objects.all().filter(team__name=team_slug)
    advantages = find_advantages(players)
    weaknesses = find_weaknesses(players)
    context = {
    	'advantages': advantages,
    	'weaknesses': weaknesses,
        'team': team,
        'players': players
    }
    return render(request, 'nba/player_by_team.html', context)

def find_advantages(players):
	points = 0
	rebounds = 0
	team_size = len(players)
	advantages = []
	if team_size == 0:
		return advantages
	for player in players:
		points += player.points
		rebounds += player.defreb + player.ofreb
	if points > 100:
		advantages.append("High Scoring")
	if rebounds > 45:
		advantages.append("Rebounding")
	return advantages

def find_weaknesses(players):
	age = 0
	points = 0
	rebounds = 0
	weight = 0
	height = 0
	team_size = len(players)
	weaknesses = []
	if team_size == 0:
		return weaknesses
	for player in players:
		age += player.age
		points += player.points
		rebounds += player.defreb + player.ofreb
		weight += player.weight
		height += find_height(player.height)
	if age // team_size > 27.0:
		weaknesses.append("Old")
	elif age // team_size < 25.0:
		weaknesses.append("Young")
	if points < 90.0:
		weaknesses.append("Lacking Firepower")
	if rebounds < 36.5:
		weaknesses.append("Poor Rebounding")
	if weight // team_size < 220:
		weaknesses.append("Scrawny")
	if height / team_size < 79:
		weaknesses.append("Short")
	return weaknesses

def find_height(string_height):
	string = ""
	true_height = 0
	for i in range(len(string_height)):
		if string_height[i].isdigit():
			string += (string_height[i])
	true_height += int(string[0]) * 12
	if len(string) == 2:
		true_height += int(string[1])
	else: 
		true_height += 10 + int(string[2])
	return true_height

    #lists players by team ordered by categories
def player_by_team_cats(request, team_slug, cat_slug):
    teams = Team.objects.filter(name=team_slug)
    team = teams[0]
    players = Player.objects.all().filter(team__name=team_slug).order_by('-' + cat_slug)
    context = {
        'team': team,
        'players': players
    }
    return render(request, 'nba/player_by_team.html', context)

def contact_us(request):
	return render(request, 'nba/contact_us.html')
