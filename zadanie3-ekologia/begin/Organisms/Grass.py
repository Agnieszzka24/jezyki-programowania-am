from .Plant import Plant


class Grass(Plant):
	'''Klasa reprezentująca trawę w ekosystemie'''

	def __init__(self, grass=None, position=None, world=None):
		'''Inicjalizuje trawę, jeśli nie podano obiektu trawy, tworzy nową instancję'''
		super(Grass, self).__init__(grass, position, world)

	def clone(self):
		'''Zwraca nową instancję trawy'''
		return Grass(self, None, None)

	def initParams(self):
		'''Inicjalizuje parametry trawy'''
		self.power = 0
		self.initiative = 0
		self.liveLength = 6
		self.powerToReproduce = 3
		self.sign = 'G'
