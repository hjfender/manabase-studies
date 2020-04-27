import enums

class SolRing():
	def __init__(self):
		self.name = 'Sol Ring'
		self.supertypes = []
		self.types = [enums.CardType.ARTIFACT]
		self.subtypes = []
		self.cmc = 1
		self.produces = 2
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class Talisman():
	def __init__(self):
		self.name = 'Talisman'
		self.supertypes = []
		self.types = [enums.CardType.ARTIFACT]
		self.subtypes = []
		self.cmc = 2
		self.produces = 1
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class ThranDynamo():
	def __init__(self):
		self.name = 'Thran Dynamo'
		self.supertypes = []
		self.types = [enums.CardType.ARTIFACT]
		self.subtypes = []
		self.cmc = 4
		self.produces = 3
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()