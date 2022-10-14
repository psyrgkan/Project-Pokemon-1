'''
This is where the class for pokemon lives.
'''
from typing import List
from attack import Attack

class Pokemon:
	'''
	Class takes in:

	stats: in list format where stats[0] is HP, stats[1] is Attack, stats[2] is Defence,
			stats[3] is Special Attack, stats[4] is Special Defence and stats[5] is Speed

	type: gives the type of the pokemon in str format ('water', 'fire', 'flying', etc.)
	'''
	def __init__(self, stats: list, tipo: str, attacks: list[Attack]):
		self.stats = stats
		self.tipo = tipo
		self.hp = stats[0]
		self.allmoves = attacks
		self.moveset = []
