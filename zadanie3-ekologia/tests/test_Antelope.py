# tests/test_Antelope.py
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'begin')))

from Organisms.Antelope import Antelope
from Position import Position
from World import World

class TestAntelope(unittest.TestCase):
    def setUp(self):
        self.world = World(10, 10)
        self.position = Position(xPosition=5, yPosition=5)
        self.antelope = Antelope(position=self.position, world=self.world)

    def test_initial_parameters(self):
        self.assertEqual(self.antelope.power, 4)
        self.assertEqual(self.antelope.sign, 'A')

    def test_escape_logic(self):
        escape_pos = self.antelope.escapeFromLynx()
        self.assertTrue(escape_pos is None or isinstance(escape_pos, Position))

if __name__ == '__main__':
    unittest.main()