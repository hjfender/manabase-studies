import enums

class RampantGrowth():
	def __init__(self):
		self.name = 'Rampant Growth'
		self.supertypes = []
		self.types = [enums.CardType.SORCERY]
		self.subtypes = []
		self.cmc = 2
		self.produces = 1
		self.requires = { 'Deck' : [[(enums.CardSupertype.BASIC, enums.CardType.LAND, 1)]]}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class Cultivate():
	def __init__(self):
		self.name = 'Cultivate'
		self.supertypes = []
		self.types = [enums.CardType.SORCERY]
		self.subtypes = []
		self.cmc = 3
		self.produces = 2
		self.requires = { 'Deck' : [[(enums.CardSupertype.BASIC, enums.CardType.LAND, 2)]]}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()