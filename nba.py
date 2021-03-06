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

	basic_player_dataset = list(zip(players, ages, positions))

	return basic_player_dataset

print(create_basic_dataset('https://basketball.realgm.com/nba/players'))