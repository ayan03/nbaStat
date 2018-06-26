from basic_list import *

#takes in a basic_list
#RIGHT NOW, JUST PRINTS OUT THE BASIC STUFF, FIGURE OUT MAP SHIT LATER
#creates a ?map? of players with basic stats(name, age, position) filled out
def basic_players():
	pbl = create_basic_dataset('https://basketball.realgm.com/nba/players')
	for player in pbl:
		print(player[0], player[1], player[2])

basic_players()