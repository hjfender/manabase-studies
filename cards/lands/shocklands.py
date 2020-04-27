import enums

class BloodCrypt():
	def __init__(self):
		self.name = 'Blood Crypt'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.SWAMP, enums.CardSubtype.MOUNTAIN]
		self.cmc = 0
		self.produces = [[(enums.Mana.BLACK, 1)],[(enums.Mana.RED, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()
		
class BreedingPool():
	def __init__(self):
		self.name = 'Breeding Pool'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.ISLAND, enums.CardSubtype.FOREST]
		self.cmc = 0
		self.produces = [[(enums.Mana.BLUE, 1)],[(enums.Mana.GREEN, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class GodlessShrine():
	def __init__(self):
		self.name = 'Godless Shrine'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.SWAMP, enums.CardSubtype.PLAINS]
		self.cmc = 0
		self.produces = [[(enums.Mana.BLACK, 1)],[(enums.Mana.WHITE, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class HallowedFountain():
	def __init__(self):
		self.name = 'Hallowed Fountain'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.PLAINS, enums.CardSubtype.ISLAND]
		self.cmc = 0
		self.produces = [[(enums.Mana.BLUE, 1)],[(enums.Mana.WHITE, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class OvergrownTomb():
	def __init__(self):
		self.name = 'Overgrown Tomb'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.SWAMP, enums.CardSubtype.FOREST]
		self.cmc = 0
		self.produces = [[(enums.Mana.BLACK, 1)],[(enums.Mana.GREEN, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class SacredFoundry():
	def __init__(self):
		self.name = 'Sacred Foundry'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.PLAINS, enums.CardSubtype.MOUNTAIN]
		self.cmc = 0
		self.produces = [[(enums.Mana.WHITE, 1)],[(enums.Mana.RED, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class SteamVents():
	def __init__(self):
		self.name = 'Steam Vents'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.ISLAND, enums.CardSubtype.MOUNTAIN]
		self.cmc = 0
		self.produces = [[(enums.Mana.BLUE, 1)],[(enums.Mana.RED, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class StompingGround():
	def __init__(self):
		self.name = 'Stomping Ground'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.FOREST, enums.CardSubtype.MOUNTAIN]
		self.cmc = 0
		self.produces = [[(enums.Mana.GREEN, 1)],[(enums.Mana.RED, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class TempleGarden():
	def __init__(self):
		self.name = 'Temple Garden'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.FOREST, enums.CardSubtype.PLAINS]
		self.cmc = 0
		self.produces = [[(enums.Mana.GREEN, 1)],[(enums.Mana.WHITE, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()

class WateryGrave():
	def __init__(self):
		self.name = 'Watery Grave'
		self.supertypes = []
		self.types = [enums.CardType.LAND]
		self.subtypes = [enums.CardSubtype.SWAMP, enums.CardSubtype.ISLAND]
		self.cmc = 0
		self.produces = [[(enums.Mana.BLACK, 1)],[(enums.Mana.BLUE, 1)]]
		self.requires = {}

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__str__()