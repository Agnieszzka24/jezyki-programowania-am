# tests/test_World.py
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'begin')))

from World import World
from Position import Position
from Organisms.Lynx import Lynx

class TestWorld(unittest.TestCase):
    def setUp(self):
        self.world = World(10, 10)

    def test_add_organism(self):
        lynx = Lynx(position=Position(xPosition=1, yPosition=1), world=self.world)
        self.assertTrue(self.world.addOrganism(lynx))

    def test_plague_activation(self):
        self.assertFalse(self.world.plague_active)
        self.world.activate_plague()  # Nie powinno się aktywować (wymaga 5 tur)
        self.assertFalse(self.world.plague_active)

if __name__ == '__main__':
    unittest.main()