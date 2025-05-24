from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
import os


if __name__ == '__main__':
	'''Główna funkcja programu, która tworzy świat i organizmy, a następnie symuluje ich interakcje'''
	pyWorld = World(10, 10)

	newOrg = Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=2, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	print(pyWorld)

	for _ in range(0, 50):
		"""Pętla symulująca tury, w której organizmy wykonują swoje ruchy i akcje."""
		input('')
		os.system('cls')
		pyWorld.makeTurn()
		print(pyWorld)
