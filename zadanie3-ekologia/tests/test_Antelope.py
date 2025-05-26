# tests/test_Antelope.py
import sys
import os
import unittest
from unittest.mock import MagicMock, patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'begin')))
from Organisms.Antelope import Antelope
from Position import Position
from World import World
from Organisms.Lynx import Lynx
from Action import Action
from ActionEnum import ActionEnum


class TestAntelope(unittest.TestCase):
    """Testy jednostkowe dla Antylopy"""
    def setUp(self):
        """Inicjalizacja testów"""
        self.world = MagicMock()
        self.position = Position(position=Position(xPosition=5, yPosition=5))
        self.antelope = Antelope(position=self.position, world=self.world)
        self.antelope.initParams()

    def test_initParams(self):
        """Sprawdzenie czy parametry antylopy są poprawne"""
        self.assertEqual(self.antelope.power, 4)
        self.assertEqual(self.antelope.initiative, 3)
        self.assertEqual(self.antelope.sign, 'A')

    def test_clone(self):
        """Sprawdzenie czy klonowanie antylopy działa poprawnie"""
        clone = self.antelope.clone()
        self.assertIsInstance(clone, Antelope)
        self.assertEqual(clone.sign, 'A')

    def test_getLynxPosition(self):
        """Sprawdzenie czy zwracane są pozycje rysia w pobliżu antylopy"""
        # Test bez rysia w pobliżu
        self.world.getNeighboringPositions.return_value = [
            Position(position=Position(xPosition=4, yPosition=5)),
            Position(position=Position(xPosition=6, yPosition=5))
        ]
        self.world.getOrganismFromPosition.return_value = None
        self.assertEqual(len(self.antelope.getLynxPosition()), 0) #brak rysia w pobliżu

        # Test z rysiem w pobliżu
        lynx = Lynx(position=Position(position=Position(xPosition=6, yPosition=5)))
        self.world.getOrganismFromPosition.side_effect = [None, lynx]
        lynx_positions = self.antelope.getLynxPosition()
        self.assertEqual(lynx_positions, [Position(position=Position(xPosition=6, yPosition=5))])

    def test_tryEscape(self):
        """Testowanie ucieczki antylopy przed rysiem"""
        lynx_pos = Position(position=Position(xPosition=6, yPosition=5))  # Ryś na prawo od antylopy 5 5

        # Udana ucieczka (wolne miejsce na lewo)
        self.world.positionOnBoard.return_value = True
        self.world.getOrganismFromPosition.return_value = None
        result = self.antelope.tryEscape([lynx_pos])
        self.assertEqual(result[0].position, Position(position=Position(xPosition=3, yPosition=5)))  # Ucieczka w lewo
    #     5 - 6 = -1 → 5 + 2*(-1) = 3


    def test_move(self):
        """Testowanie ruchu antylopy"""
        # Normalny ruch bez rysia
        self.antelope.getLynxPosition = MagicMock(return_value=[])
        self.antelope.getNeighboringPosition = MagicMock(return_value=[Position(position=Position(xPosition=5, yPosition=6))])
        actions = self.antelope.move()
        self.assertEqual(actions[0].position, Position(position=Position(xPosition=5, yPosition=6)))

        # Ruch z ucieczką przed rysiem
        self.antelope.getLynxPosition = MagicMock(return_value=[Position(position=Position(xPosition=6, yPosition=5))])
        self.antelope.tryEscape = MagicMock(return_value=[Action(ActionEnum.A_MOVE, Position(position=Position(xPosition=3, yPosition=5)), 0, self.antelope)])
        actions = self.antelope.move()
        self.assertEqual(actions[0].position, Position(position=Position(xPosition=3, yPosition=5)))




if __name__ == '__main__':
    unittest.main()