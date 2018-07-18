from pandas import DataFrame, read_csv

import pandas as pd
import requests
from bs4 import BeautifulSoup


#creates a list of players with respective age and positions
#takes in (string) url 
#returns a list of ("name", age, "position")
def create_basic_dataset(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.content, 'lxml')
	table = soup.find_all('table')[0]
	df = pd.read_html(str(table))[0]

	#creates a list of player names
	players = df["Player"].tolist()

	#creates a list of player ages
	ages = df["Age"].tolist()

	#creates a list of player positions
	positions = df["Pos"].tolist()

	#creates a list of player heights
	height = df["HT"].tolist()

	#creates a list of player weights
	weight = df["WT"].tolist()

	#creates a list of player teams
	team = df["Current Team"].tolist()

	basic_player_dataset = list(zip(players, ages, positions, height, weight, team))

	return basic_player_dataset

def fill_basic_dataset(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'lxml')
	table = soup.find_all('table')
	#returns a list of data frames
	df = pd.read_html(str(table))[0]
	df = df[df['Player'] != 'Player']
	df = filter_frame(df)

	#creates a list of player class attributes
	players = df['Player'].tolist()

	age = df['Age'].tolist()

	positions = df['Pos'].tolist()

	team = df['Tm'].tolist()

	gamesPlayed = df['G'].tolist()

	minutes = df['MP'].tolist()

	shootingPct = df['FG%'].tolist()

	threeptPct = df['3P%'].tolist()

	ftPct = df['FT%'].tolist()

	ftAttempts = df['FTA'].tolist()

	averageRb = df['TRB'].tolist()

	averageAst = df['AST'].tolist()

	averageSt = df['STL'].tolist()

	averageTo = df['TOV'].tolist()

	personalFouls = df['PF'].tolist()

	ppg = df['PS/G'].tolist()

	fill_set = list(zip(players, age, positions, team, gamesPlayed, minutes, shootingPct, threeptPct,
	ftPct, ftAttempts, averageRb, averageAst, averageSt, averageTo, personalFouls, ppg))

	return fill_set

	#takes in a dataframe and filters out duplicate players and aggregates stats
def filter_frame(df):
	player_list = df["Player"].tolist()

	#returns a list of duplicates: stats for players that have switched teams
	duplicate = list(set([x for x in player_list if player_list.count(x) > 1]))

	for dup in duplicate:
		sub_frame = df[df['Player'].str.contains(dup)]
		df = df[df.Player != dup]
		sub_frame.iloc[0].Tm = sub_frame.iloc[-1].Tm
		sub_frame = sub_frame[:1]
		df = df.append(sub_frame, ignore_index = True)
		
	"""
	df = df[df.Player != 'Isaiah Thomas']
	sub_frame.iloc[0].Tm = sub_frame.iloc[-1].Tm
	sub_frame = sub_frame[:1]
	df = df.append(sub_frame, ignore_index = True)
	"""

	return df



	





	

#tester
#print(create_basic_dataset('https://basketball.realgm.com/nba/players'))

#print(filter_frame(fill_basic_dataset('https://www.basketball-reference.com/leagues/NBA_2018_per_game.html')))
#print(fill_basic_dataset('https://www.basketball-reference.com/leagues/NBA_2018_per_game.html'))
