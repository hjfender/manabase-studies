import enums

class FloodPlain():
	def __init__(self):
		self.name = 'Flood Plain'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.ISLAND, enums.CardType.LAND, 1)],[(enums.CardSubtype.PLAINS, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class BadRiver():
	def __init__(self):
		self.name = 'Bad River'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.ISLAND, enums.CardType.LAND, 1)],[(enums.CardSubtype.SWAMP, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class RockyTarPit():
	def __init__(self):
		self.name = 'Rocky Tar Pit'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.MOUNTAIN, enums.CardType.LAND, 1)],[(enums.CardSubtype.SWAMP, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class MoutainValley():
	def __init__(self):
		self.name = 'Mountain Valley'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.MOUNTAIN, enums.CardType.LAND, 1)],[(enums.CardSubtype.FOREST, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class Grasslands():
	def __init__(self):
		self.name = 'Grasslands'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.PLAINS, enums.CardType.LAND, 1)],[(enums.CardSubtype.FOREST, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class FloodedStrand():
	def __init__(self):
		self.name = 'Flooded Strand'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.ISLAND, enums.CardType.LAND, 1)],[(enums.CardSubtype.PLAINS, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class PollutedDelta():
	def __init__(self):
		self.name = 'Polluted Delta'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.ISLAND, enums.CardType.LAND, 1)],[(enums.CardSubtype.SWAMP, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class BloodstainedMire():
	def __init__(self):
		self.name = 'Bloodstained Mire'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.MOUNTAIN, enums.CardType.LAND, 1)],[(enums.CardSubtype.SWAMP, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class WoodedFoothills():
	def __init__(self):
		self.name = 'Wooded Foothills'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.MOUNTAIN, enums.CardType.LAND, 1)],[(enums.CardSubtype.FOREST, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class WindsweptHeath():
	def __init__(self):
		self.name = 'Windswept Heath'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.PLAINS, enums.CardType.LAND, 1)],[(enums.CardSubtype.FOREST, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class MarshFlats():
	def __init__(self):
		self.name = 'Marsh Flats'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.PLAINS, enums.CardType.LAND, 1)],[(enums.CardSubtype.SWAMP, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class ScaldingTarn():
	def __init__(self):
		self.name = 'Scalding Tarn'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.ISLAND, enums.CardType.LAND, 1)],[(enums.CardSubtype.MOUNTAIN, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class VerdantCatacombs():
	def __init__(self):
		self.name = 'Verdant Catacombs'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.FOREST, enums.CardType.LAND, 1)],[(enums.CardSubtype.SWAMP, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class AridMesa():
	def __init__(self):
		self.name = 'Arid Mesa'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.MOUNTAIN, enums.CardType.LAND, 1)],[(enums.CardSubtype.PLAINS, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class MistyRainforest():
	def __init__(self):
		self.name = 'Misty Rainforest'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = []
		self.cmc = 0
		self.produces = []
		self.requires = { 'Deck' : [[(enums.CardSubtype.ISLAND, enums.CardType.LAND, 1)],[(enums.CardSubtype.FOREST, enums.CardType.LAND, 1)]] }

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()