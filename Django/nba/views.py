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
			return render(request, 'nba/search_results.html', {'players': players, 'query': name})
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
def player_by_team(request, team_slug):
    teams = Team.objects.filter(name=team_slug)
    team = teams[0]
    players = Player.objects.all().filter(team__name=team_slug)
    context = {
        'team': team,
        'players': players
    }
    return render(request, 'nba/player_by_team.html', context)

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
