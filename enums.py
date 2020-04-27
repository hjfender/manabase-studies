from enum import Enum

class CardSupertype(Enum):
	BASIC = 1
	LEGENDARY = 2
	SNOW = 3

class CardType(Enum):
	LAND = 1
	CREATURE = 2
	ARTIFACT = 3
	ENCHANTMENT = 4
	PLANESWALKER = 5
	INSTANT = 6
	SORCERY = 7

class CardSubtype(Enum):
	# Lands
	PLAINS = 1
	ISLAND = 2
	SWAMP = 3
	MOUNTAIN = 4
	FOREST = 5
	URZAS = 6
	MINE = 7
	POWERPLANT = 8
	TOWER = 9
	# Planeswalkers
	CHANDRA = 10
	DOMRI = 11
	NISSA = 12
	UGIN = 13
	XENAGOS = 14
	# Creatures

class Mana(Enum):
	WHITE = 1
	BLUE = 2
	BLACK = 3
	RED = 4
	GREEN = 5
	COLORLESS = 6

class Tag(Enum):
	MANAPRODUCING = 1
