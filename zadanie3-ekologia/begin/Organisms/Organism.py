from abc import ABC, abstractmethod
from Position import Position
from Action import Action
from ActionEnum import ActionEnum


class Organism(ABC):
	'''Klasa bazowa dla wszystkich organizmów w ekosystemie'''

	def __init__(self, organism, position, world):
		'''Inicjalizuje organizm, jeśli nie podano obiektu organizmu, tworzy nową instancję'''
		self.__power = None
		self.__initiative = None
		self.__position = None
		self.__liveLength = None
		self.__powerToReproduce = None
		self.__sign = None
		self.__world = None

		if organism is not None:
			self.__power = organism.power
			self.__initiative = organism.initiative
			self.__position = organism.position
			self.__liveLength = organism.liveLength
			self.__powerToReproduce = organism.powerToReproduce
			self.__sign = organism.sign
			self.__world = organism.__world
		else:
			if position is not None:
				self.__position = position
			if world is not None:
				self.__world = world
			self.initParams()


	@property
	def power(self):
		'''Zwraca moc organizmu'''
		return self.__power

	@power.setter
	def power(self, value):
		'''Ustawia moc organizmu'''
		self.__power = value

	@property
	def initiative(self):
		'''Zwraca inicjatywę organizmu'''
		return self.__initiative

	@initiative.setter
	def initiative(self, value):
		'''Ustawia inicjatywę organizmu'''
		self.__initiative = value

	@property
	def position(self):
		'''Zwraca pozycję organizmu na planszy'''
		return self.__position

	@position.setter
	def position(self, value):
		'''Ustawia pozycję organizmu na planszy'''
		self.__position = value

	@property
	def liveLength(self):
		'''Zwraca długość życia organizmu'''
		return self.__liveLength

	@liveLength.setter
	def liveLength(self, value):
		'''Ustawia długość życia organizmu'''
		self.__liveLength = value

	@property
	def powerToReproduce(self):
		'''Zwraca moc potrzebną do rozmnażania się organizmu'''
		return self.__powerToReproduce

	@powerToReproduce.setter
	def powerToReproduce(self, value):
		'''Ustawia moc potrzebną do rozmnażania się organizmu'''
		self.__powerToReproduce = value

	@property
	def sign(self):
		'''Zwraca znak reprezentujący organizm na planszy'''
		return self.__sign

	@sign.setter
	def sign(self, value):
		'''Ustawia znak reprezentujący organizm na planszy'''
		self.__sign = value

	@property
	def world(self):
		'''Zwraca świat, w którym organizm się znajduje'''
		return self.__world

	@world.setter
	def world(self, value):
		'''Ustawia świat, w którym organizm się znajduje'''
		self.__world = value

	@abstractmethod
	def move(self):
		'''Zwraca listę akcji ruchu organizmu'''
		pass

	@abstractmethod
	def action(self):
		'''Zwraca listę akcji, które organizm może wykonać'''
		pass

	@abstractmethod
	def initParams(self):
		'''Inicjalizuje parametry organizmu'''
		pass

	@abstractmethod
	def clone(self):
		'''Tworzy kopię organizmu'''
		pass

	def consequences(self, atackingOrganism):
		'''Zwraca konsekwencje ataku innego organizmu na ten organizm'''
		result = []

		if self.power > atackingOrganism.power:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
		else:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
		return result

	def ifReproduce(self):
		'''Sprawdza, czy organizm może się rozmnożyć'''
		result = False

		if self.power >= self.powerToReproduce:
			result = True
		return result

	def __str__(self):
		'''Zwraca reprezentację tekstową organizmu'''
		return '{0}: power: {1} initiative: {2} liveLength {3} position: {4}'\
				.format(self.__class__.__name__, self.power, self.initiative, self.liveLength, self.position)
