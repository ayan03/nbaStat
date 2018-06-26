class Player:

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
		self.shootingPct = None
		self.threeptPct = None
		self.fantasyScore = None

	def __repr__(self):
		return "{!r}".format(self.name)

	def __eq__(self, other):
		return (type(other) == Player and self.name == other.name and self.position == other.position)

	#basic statline
	def statLine(self): 
		if age == None and height == None and weight == None and team == None:
			print("Player information needs to be updated")
		else:
			#not complete
			print ("Name: ", self.name, ", Position: ", self.position, ", Team: ", self.team, ", Age: ", self.age, ", Height: ", self.height)
	


	#calculates the total ESPN fantasy basketball points
	def calcFScore(self):
		total = 0




