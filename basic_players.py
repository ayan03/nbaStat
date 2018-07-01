from basic_list import *
from player import *

#takes in a basic_list
#RIGHT NOW, JUST RETURNS A LIST OUT THE BASIC STUFF, FIGURE OUT MAP SHIT LATER
#creates a ?map? of players with basic stats(name, age, position) filled out
def basic_players():
	players = []
	pbl = create_basic_dataset('https://basketball.realgm.com/nba/players')
	for player in pbl:
		nba_player = Player(player[0], player[1], player[2])

		#sets the height and weight field for each player
		nba_player.height = player[3]
		nba_player.weight = player[4]
		nba_player.team = player[5]

		players.append(nba_player)
	return players

def mod_list(player_list):

#takes in a list of players for formatting each field and returns a formatted list
def format_list(player_list):
	for player in player_list:
		#formats height from 6-6 to 6'6"
		player.height = """ {ft}'{inch}" """.format(ft = player.height[0], inch = player.height[2])
	return player_list


#tester
#print(basic_players()[0].height)
print(format_list(basic_players())[0].statLine())