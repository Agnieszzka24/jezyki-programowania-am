from .Organism import Organism
from Action import Action
from ActionEnum import ActionEnum
import random


class Animal(Organism):
	'''Klasa reprezentująca zwierzę w ekosystemie (dziediczy po Organism)'''

	def __init__(self, animal=None, position=None, world=None):
		'''Inicjalizuje zwierzę, jeśli nie podano obiektu zwierzęcia, tworzy nową instancję'''
		super(Animal, self).__init__(animal, position, world)
		self.__lastPosition = position

	@property
	def lastPosition(self):
		'''Zwraca ostatnią pozycję zwierzęcia'''
		return self.__lastPosition

	@lastPosition.setter
	def lastPosition(self, value):
		'''Ustawia ostatnią pozycję zwierzęcia'''
		self.__lastPosition = value

	def move(self):
		'''Wykonuje ruch zwierzęcia na losowe sąsiednie pole.
		Obsługuje kolizje z innymi organizmami i zwraca odpowiednie akcje.'''
		result = []
		pomPositions = self.getNeighboringPosition()
		newPosition = None

		if pomPositions:
			newPosition = random.choice(pomPositions)
			result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
			self.lastPosition = self.position
			metOrganism = self.world.getOrganismFromPosition(newPosition)
			if metOrganism is not None:
				result.extend(metOrganism.consequences(self))
		return result

	def action(self):
		'''Próbuje rozmnożyć zwierzę, jeśli spełnione są warunki.
		   Dodaje nowe zwierzę na sąsiednim wolnym polu.'''
		result = []
		newAnimal = None
		birthPositions = self.getNeighboringBirthPosition()

		if self.ifReproduce() and birthPositions:
			newAnimalPosition = random.choice(birthPositions)
			newAnimal = self.clone()
			newAnimal.initParams()
			newAnimal.position = newAnimalPosition
			self.power = self.power / 2
			result.append(Action(ActionEnum.A_ADD, newAnimalPosition, 0, newAnimal))
		return result

	def getNeighboringPosition(self):
		'''Zwraca listę sąsiednich pozycji zwierzęcia'''
		return self.world.getNeighboringPositions(self.position)

	def getNeighboringBirthPosition(self):
		'''Zwraca listę wolnych sąsiednich pozycji, na których zwierzę może się rozmnożyć'''
		return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))
