class Player:

	#imperial units
	def __init__(self, name, age, position):
		self.name = name
		self.position = position
		self.age = age
		self.height = None
		self.weight = None
		self.team = None
		self.averagePts = None
		self.averageAst = None
		self.averageRb = None
		self.averageBk = None
		self.averageTo = None
		self.averageSt = None
		self.shootingPct = None
		self.threeptPct = None
		self.ftPct = None
		self.ftAttempts = None
		self.fantasyScore = None

	def __repr__(self):
		return "{!r}".format(self.name)

	def __eq__(self, other):
		return (type(other) == Player and self.name == other.name and self.position == other.position)

	#basic statline
	def statLine(self): 
		if self.age == None and self.height == None and self.weight == None and self.team == None:
			print("Player information needs to be updated")
			return False
		else:
			print ("Name: ", self.name, ", Position: ", self.position, ", Team: ", self.team, ", Average Points: ", self.averagePts, ", Average Assists: ", self.averageAst, ", Average Rebounds: ", self.averageRb)	
			return True			

	#calculates the total ESPN fantasy basketball points for the player
	#based on 2017 - 2018 scoring season
	def calcFScore(self):
		total = 0
		reboundsPt = self.averageRb * 1.2
		assistPt = self.averageAst * 1.5
		scorePt = self.averagePts + (self.ftPct * self.ftAttempts)
		blockPt = self.averageBk * 3
		stealPt = self.averageSt * 3
		turnoverPt = self.averageTo 
		total = total + reboundsPt + assistPt + scorePt + blockPt + stealPt - turnoverPt
		self.fantasyScore = total






