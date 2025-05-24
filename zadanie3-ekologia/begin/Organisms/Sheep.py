from .Animal import Animal


class Sheep(Animal):
	'''Klasa reprezentująca owcę w ekosystemie'''

	def __init__(self, sheep=None, position=None, world=None):
		'''Inicjalizuje owcę, jeśli nie podano obiektu owcy, tworzy nową instancję'''
		super(Sheep, self).__init__(sheep, position, world)

	def clone(self):
		'''Zwraca nową instancję owcy'''
		return Sheep(self, None, None)

	def initParams(self):
		'''Inicjalizuje parametry owcy'''
		self.power = 3
		self.initiative = 3
		self.liveLength = 10
		self.powerToReproduce = 6
		self.sign = 'S'

	def getNeighboringPosition(self):
		'''Zwraca listę sąsiednich pozycji owcy, które nie są zajęte przez inne zwierzęta'''
		return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))
