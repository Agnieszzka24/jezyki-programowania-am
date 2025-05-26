# tests/test_Lynx.py
import sys
import os
import unittest
from unittest.mock import MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'begin')))

from Organisms.Lynx import Lynx
from Position import Position
from World import World

class TestLynx(unittest.TestCase):
    """Testy jednostkowe dla Rysia"""
    def setUp(self):
        """Inicjalizacja testów"""
        self.world = World(10, 10)
        self.position = Position(xPosition=5, yPosition=5)
        self.lynx = Lynx(position=self.position, world=self.world)

    def test_initParams(self):
        """Sprawdzenie czy parametry rysia są poprawnie inicjalizowane"""
        self.assertEqual(self.lynx.power, 6)
        self.assertEqual(self.lynx.initiative, 5)
        self.assertEqual(self.lynx.sign, 'R')

    def test_clone(self):
        """Sprawdzenie czy klonowanie rysia działa poprawnie"""
        clone = self.lynx.clone()
        self.assertIsInstance(clone, Lynx)
        self.assertEqual(clone.sign, 'R')

    def test_getNeighboringPosition(self):
        """Sprawdzenie czy zwracane są sąsiednie pozycje rysia, które nie są zajęte przez inne zwierzęta"""
        # Mockujemy świat, aby zwracał tylko wolne pola
        self.world.filterPositionsWithoutAnimals = MagicMock(return_value=[
            Position(position=Position(xPosition=6, yPosition=5)),
            Position(position=Position(xPosition=4, yPosition=5))
        ])
        neighbors = self.lynx.getNeighboringPosition()
        self.assertEqual(len(neighbors), 2)

if __name__ == '__main__':
    unittest.main()