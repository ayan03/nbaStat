class Player:

	def __init__(self, name, position):
		self.name = name
		self.position = position
		self.age = None
		self.height = None
		self.weight = None
		self.team = None
		self.averagePts = None
		self.averageAst = None
		self.averageRb = None
		self.shootingPct = None
		self.threeptPct = None
		self.fantasyScore = None

	def statLine(self): 
		if age == None and height == None and weight == None and team == None:
			print("Player information needs to be updated")
		else:
			#not complete
			print ("Name: ", self.name, ", Position: ", self.position, ", Team: ", self.team, ", Age: ", self.age, ", Height: ", self.height)
		
	def calcFScore(self):
		total = 0




