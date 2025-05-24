from .Animal import Animal


class Lynx(Animal):
    '''Klasa reprezentująca rysia w ekosystemie'''

    def __init__(self, lynx=None, position=None, world=None):
        '''Inicjalizuje rysia, jeśli nie podano obiektu rysia, tworzy nową instancję'''
        super(Lynx, self).__init__(lynx, position, world)

    def clone(self):
        '''Zwraca nową instancję rysia'''
        return Lynx(self, None, None)

    def initParams(self):
        '''Inicjalizuje parametry rysia'''
        self.power = 6
        self.initiative = 5
        self.liveLength = 18
        self.powerToReproduce = 14
        self.sign = 'R'

    def getNeighboringPosition(self):
        '''Zwraca listę sąsiednich pozycji rysia, które nie są zajęte przez inne zwierzęta'''
        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))