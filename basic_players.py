from basic_list import *
from player import *

#takes in a basic_list
#RIGHT NOW, JUST RETURNS A LIST OUT THE BASIC STUFF, FIGURE OUT MAP SHIT LATER
#creates a ?map? of players with basic stats(name, age, position) filled out
def basic_players():
	players = []
	pbl = create_basic_dataset('https://basketball.realgm.com/nba/players')
	for player in pbl:
		players.append(Player(player[0], player[1], player[2]))
	return players


#tester
print(basic_players()[10].position)