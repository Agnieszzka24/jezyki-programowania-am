from enum import Enum


class ActionEnum(Enum):
	'''Enum reprezentujący różne typy akcji wykonywanych przez organizmy w ekosystemie
	Definiuje dostępne typy akcji jako stałe symboliczne (np. A_MOVE, A_ADD)'''

	A_MOVE = 0
	A_REMOVE = 1
	A_ADD = 2
	A_INCREASEPOWER = 3
