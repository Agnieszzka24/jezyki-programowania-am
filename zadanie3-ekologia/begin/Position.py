

class Position(object):
	'''Klasa reprezentująca pozycję na planszy w ekosystemie'''

	def __init__(self, position = None, xPosition = None, yPosition = None):
		'''Inicjalizuje pozycję, jeśli nie podano obiektu pozycji, tworzy nową instancję'''
		self.__x = 0
		self.__y = 0

		if position is not None:
			self.__x = position.x
			self.__y = position.y
		else:
			if xPosition is not None:
				self.__x = xPosition
			if yPosition is not None:
				self.__y = yPosition

	@property
	def x(self):
		'''Zwraca współrzędną x pozycji'''
		return self.__x

	@x.setter
	def x(self, value):
		'''Ustawia współrzędną x pozycji'''
		self.__x = value

	@property
	def y(self):
		'''Zwraca współrzędną y pozycji'''
		return self.__y

	@y.setter
	def y(self, value):
		'''Ustawia współrzędną y pozycji'''
		self.__y = value

	def __eq__(self, other):
		'''Porównuje dwie pozycje na planszy'''
		return (self.x == other.x) and (self.y == other.y)

	def __str__(self):
		'''Zwraca reprezentację pozycji jako ciąg znaków'''
		return '({0}, {1})'.format(self.x, self.y)
