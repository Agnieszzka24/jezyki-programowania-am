from .Animal import Animal
from Position import Position
from Action import Action
from ActionEnum import ActionEnum

class Antelope(Animal):
    """Klasa reprezentująca Antylopę w ekosystemie"""

    def __init__(self, antelope=None, position=None, world=None):
        """Inicjalizuje Antylopę, przyjmuje opcionalne parametry do klonowania lub ustawienia pozycji i świata"""
        super(Antelope, self).__init__(antelope, position, world)

    def clone(self):
        """Zwraca nową instancję Antylopy - klonuje obecny obiekt (do rozmnażania)"""
        return Antelope(self, None, None)

    def initParams(self):
        """Inicjalizuje parametry Antylopy"""
        self.power = 4
        self.initiative = 3
        self.liveLength = 11
        self.powerToReproduce = 5
        self.sign = 'A'

    def move(self):
        """Sprawdza, czy w pobliżu jest ryś, jaśli tak, to próbujemy uciec, jak nie, to wykonujemy normalny ruch"""
        result = []
        lynxPositions = self.getLynxPosition()

        if lynxPositions:
            result.extend(self.tryEscape(lynxPositions))
        else:
            result = super().move()

        return result

    def tryEscape(self, lynxPositions):
        """Próbuje uciec przed rysiem, jeśli jest w pobliżu i jest to możliwe"""
        result = []
        lynxPos = lynxPositions[0]  # bierzemy pierwszego napotkanego rysia
        # Obliczamy kierunek wektora ucieczki: różnica między pozycją organizmu a pozycją rysia
        dx = self.position.x - lynxPos.x
        dy = self.position.y - lynxPos.y

        # Uciekamy w przeciwnym kierunku (o 2 pola)
        escapePos = Position(xPosition=self.position.x + 2 * dx,
                           yPosition=self.position.y + 2 * dy)

        # Sprawdzamy, czy pozycja jest w granicach planszy i czy jest wolna
        if (self.world.positionOnBoard(escapePos) and
            self.world.getOrganismFromPosition(escapePos) is None):
            result.append(Action(ActionEnum.A_MOVE, escapePos, 0, self))
            self.lastPosition = self.position
        else:
            # Jeśli ucieczka nie możliwa, atakujemy rysia
            lynx = self.world.getOrganismFromPosition(lynxPos)
            if lynx:
                result.extend(lynx.consequences(self))
        return result

    def getNeighboringPosition(self):
        """Zwraca listę sąsiednich pozycji Antylopy, które nie są zajęte przez inne zwierzęta"""
        return self.world.filterPositionsWithoutAnimals(
            self.world.getNeighboringPositions(self.position))

    def getLynxPosition(self):
        """Zwraca listę pozycji rysi sąsiadujących z Antylopą"""
        neighboring = self.world.getNeighboringPositions(self.position)
        lynxPositions = []
        for pos in neighboring:
            org = self.world.getOrganismFromPosition(pos)
            if org and org.__class__.__name__ == 'Lynx':
                lynxPositions.append(pos)
        return lynxPositions