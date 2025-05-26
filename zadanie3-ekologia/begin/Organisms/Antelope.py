from .Animal import Animal
from Position import Position
from Action import Action
from ActionEnum import ActionEnum
import random

class Antelope(Animal):
    """Klasa reprezentująca Antylopę w ekosystemie"""

    def __init__(self, antelope=None, position=None, world=None):
        super(Antelope, self).__init__(antelope, position, world)

    def clone(self):
        return Antelope(self, None, None)

    def initParams(self):
        self.power = 4
        self.initiative = 3
        self.liveLength = 11
        self.powerToReproduce = 5
        self.sign = 'A'

    def escapeFromLynx(self):
        """Specjalna metoda ucieczki przed rysiem"""
        directions = [
            Position(xPosition=0, yPosition=-2),  # góra
            Position(xPosition=0, yPosition=2),  # dół
            Position(xPosition=-2, yPosition=0),  # lewo
            Position(xPosition=2, yPosition=0),  # prawo
            Position(xPosition=-2, yPosition=-2),  # lewo-góra
            Position(xPosition=2, yPosition=-2),  # prawo-góra
            Position(xPosition=-2, yPosition=2),  # lewo-dół
            Position(xPosition=2, yPosition=2)  # prawo-dół
        ]

        possible_escapes = []
        for direction in directions:
            new_pos = Position(
                xPosition=self.position.x + direction.x,
                yPosition=self.position.y + direction.y
            )
            if (self.world.positionOnBoard(new_pos) and
                    self.world.getOrganismFromPosition(new_pos) is None):
                possible_escapes.append(new_pos)

        return random.choice(possible_escapes) if possible_escapes else None

    def move(self):
        """Nadpisana metoda ruchu z uwzględnieniem ucieczki przed rysiem"""
        # Najpierw sprawdź czy w pobliżu jest ryś
        neighboring_positions = self.world.getNeighboringPositions(self.position)
        lynx_nearby = any(
            org for pos in neighboring_positions
            if (org := self.world.getOrganismFromPosition(pos))
            and org.__class__.__name__ == 'Lynx'
        )

        if lynx_nearby:
            escape_pos = self.escapeFromLynx()
            if escape_pos is not None:  # sprawdź, czy ucieczka jest możliwa
                self.lastPosition = self.position
                return [Action(
                    action=ActionEnum.A_MOVE,
                    position=escape_pos,
                    value=0,
                    organism=self
                )]
            # Jeśli ucieczka nie jest możliwa, wykonaj normalny ruch

        # Normalny ruch zwierzęcia
        pomPositions = self.getNeighboringPosition()
        if pomPositions:
            newPosition = random.choice(pomPositions)
            self.lastPosition = self.position
            result = [Action(ActionEnum.A_MOVE, newPosition, 0, self)]
            metOrganism = self.world.getOrganismFromPosition(newPosition)
            if metOrganism is not None:
                result.extend(metOrganism.consequences(self))
            return result
        return []  # Brak możliwości ruchu

    def consequences(self, attackingOrganism):
        """Specjalne zachowanie przy ataku"""
        if attackingOrganism.__class__.__name__ == 'Lynx':
            # 50% szans na ucieczkę przed rysiem
            if random.random() < 0.5:
                escape_pos = self.escapeFromLynx()
                if escape_pos is not None:
                    self.position = escape_pos
                    return []  # udana ucieczka
        return super().consequences(attackingOrganism)