import enums

class Forest():
	def __init__(self):
		self.name = 'Forest'
		self.supertypes = [enums.CardSupertype.BASIC]
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.FOREST]
		self.cmc = 0
		self.produces = [[(enums.Mana.GREEN, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class Island():
	def __init__(self):
		self.name = 'Island'
		self.supertypes = [enums.CardSupertype.BASIC]
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.ISLAND]
		self.cmc = 0
		self.produces = [[(enums.Mana.BLUE, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class Mountain():
	def __init__(self):
		self.name = 'Mountain'
		self.supertypes = [enums.CardSupertype.BASIC]
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.MOUNTAIN]
		self.cmc = 0
		self.produces = [[(enums.Mana.RED, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.__str__()

class Plains():
	def __init__(self):
		self.name = 'Plain'
		self.supertypes = [enums.CardSupertype.BASIC]
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.PLAINS]
		self.cmc = 0
		self.produces = [[(enums.Mana.WHITE, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.__str__()

class Swamp():
	def __init__(self):
		self.name = 'Swamp'
		self.supertypes = [enums.CardSupertype.BASIC]
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.SWAMP]
		self.cmc = 0
		self.produces = [[(enums.Mana.BLACK, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()