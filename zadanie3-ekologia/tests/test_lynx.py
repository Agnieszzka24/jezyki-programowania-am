# tests/test_Lynx.py
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'begin')))

from Organisms.Lynx import Lynx
from Position import Position
from World import World

class TestLynx(unittest.TestCase):
    def setUp(self):
        self.world = World(10, 10)
        self.position = Position(xPosition=5, yPosition=5)
        self.lynx = Lynx(position=self.position, world=self.world)

    def test_initial_parameters(self):
        self.assertEqual(self.lynx.power, 6)
        self.assertEqual(self.lynx.initiative, 5)
        self.assertEqual(self.lynx.sign, 'R')

    def test_clone(self):
        clone = self.lynx.clone()
        self.assertIsInstance(clone, Lynx)
        self.assertEqual(clone.sign, 'R')

if __name__ == '__main__':
    unittest.main()