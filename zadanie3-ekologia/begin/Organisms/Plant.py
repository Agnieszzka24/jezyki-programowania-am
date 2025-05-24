from .Organism import Organism
from Action import Action
from ActionEnum import ActionEnum
import random


class Plant(Organism):
	'''Klasa reprezentująca roślinę w ekosystemie (dziedziczy po Organism)'''

	def __init__(self, plant=None, position=None, world=None):
		'''Inicjalizuje roślinę, jeśli nie podano obiektu rośliny, tworzy nową instancję'''
		super(Plant, self).__init__(plant, position, world)

	def move(self):
		'''Rośliny nie poruszają się, więc ta metoda zwraca pustą listę'''
		result = []
		return result

	def action(self):
		'''Zwraca listę akcji, które roślina może wykonać'''
		result = []
		newPlant = None
		newPosition = None

		if self.ifReproduce():
			pomPositions = self.getFreeNeighboringPosition(self.position)

			if pomPositions:
				newPosition = random.choice(pomPositions)
				newPlant = self.clone()
				newPlant.initParams()
				newPlant.position = newPosition
				self.power = self.power / 2
				result.append(Action(ActionEnum.A_ADD, newPosition, 0, newPlant))
		return result

	def getFreeNeighboringPosition(self, position):
		'''Zwraca listę wolnych pozycji sąsiadujących'''
		return self.world.filterFreePositions(self.world.getNeighboringPositions(position))
