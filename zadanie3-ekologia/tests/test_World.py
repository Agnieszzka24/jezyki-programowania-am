import sys
import os
import unittest
from unittest.mock import MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'begin')))

from World import World
from Position import Position
from Organisms.Lynx import Lynx
from Organisms.Antelope import Antelope

class TestWorld(unittest.TestCase):
    def setUp(self):
        """Inicjalizacja testów"""
        self.world = World(10, 10)

    def test_addOrganism(self):
        """Test dodawania organizmu do świata"""
        lynx = Lynx(position=Position(position=Position(xPosition=1, yPosition=1)), world=self.world)
        self.assertTrue(self.world.addOrganism(lynx))

    def test_activate_plague(self):
        """Test aktywacji zarazy"""
        self.world._World__turns_since_last_plague = 5  # Wymuszamy możliwość aktywacji
        self.assertTrue(self.world.activate_plague())
        self.assertTrue(self.world.plague_active)

    def test_makeTurn(self):
        """Test wykonania tury w świecie"""
        antelope = Antelope(position=Position(position=Position(xPosition=2, yPosition=2)), world=self.world)
        self.world.addOrganism(antelope)
        self.world.makeTurn()
        self.assertEqual(self.world.turn, 1)

    def test_getOrganismFromPosition(self):
        """Test pobierania organizmu z danej pozycji"""
        lynx = Lynx(position=Position(position=Position(xPosition=3, yPosition=3)), world=self.world)
        self.world.addOrganism(lynx)
        found = self.world.getOrganismFromPosition(Position(position=Position(xPosition=3, yPosition=3)))
        self.assertEqual(found, lynx)

if __name__ == '__main__':
    unittest.main()
