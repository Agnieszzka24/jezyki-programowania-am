from Position import Position
from Organisms.Plant import Plant
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Antelope import Antelope
from Organisms.Lynx import Lynx
from Action import Action
from ActionEnum import ActionEnum


class World(object):
    '''Klasa reprezentująca świat, w którym żyją organizmy'''

    def __init__(self, worldX, worldY):
        '''Inicjalizuje świat o podanych wymiarach'''
        self.__worldX = worldX
        self.__worldY = worldY
        self.__turn = 0
        self.__organisms = []
        self.__newOrganisms = []
        self.__separator = ' o '
        # Dodane pola dla funkcjonalności plagi
        self.__plague_active = False
        self.__plague_turns_remaining = 0
        self.__turns_since_last_plague = 0
        # Lista dostępnych typów organizmów do dodania
        self.__available_organisms = {
            'G': Grass,
            'S': Sheep,
            'A': Antelope,
            'R': Lynx
        }

    @property
    def plague_active(self):
        '''Zwraca informację czy plaga jest aktywna'''
        return self.__plague_active

    @property
    def turns_since_last_plague(self):
        '''Zwraca liczbę tur od ostatniej plagi'''
        return self.__turns_since_last_plague

    def activate_plague(self):
        '''Aktywuje plagę na 2 tury, jeśli minęło co najmniej 5 tur od ostatniej plagi'''
        if self.__turns_since_last_plague >= 5 and not self.__plague_active:
            self.__plague_active = True
            self.__plague_turns_remaining = 2
            print("Plaga została aktywowana na 2 tury!")
            return True
        print("Plaga nie może być teraz aktywowana.")
        return False

    @property
    def worldX(self):
        '''Zwraca szerokość świata'''
        return self.__worldX

    @property
    def worldY(self):
        '''Zwraca wysokość świata'''
        return self.__worldY

    @property
    def turn(self):
        '''Zwraca aktualną turę świata'''
        return self.__turn

    @turn.setter
    def turn(self, value):
        '''Ustawia aktualną turę świata'''
        self.__turn = value

    @property
    def organisms(self):
        '''Zwraca listę organizmów w świecie'''
        return self.__organisms

    @organisms.setter
    def organisms(self, value):
        '''Ustawia listę organizmów w świecie'''
        self.__organisms = value

    @property
    def newOrganisms(self):
        '''Zwraca listę nowych organizmów, które mają zostać dodane do świata'''
        return self.__newOrganisms

    @newOrganisms.setter
    def newOrganisms(self, value):
        '''Ustawia listę nowych organizmów, które mają zostać dodane do świata'''
        self.__newOrganisms = value

    @property
    def separator(self):
        '''Zwraca separator używany do reprezentacji pustych pól na planszy'''
        return self.__separator

    def makeTurn(self):
        '''Wykonuje jedną turę w świecie, aktualizując pozycje i akcje organizmów'''
        # Obsługa plagi
        if self.__plague_active:
            for org in self.organisms:
                org.liveLength = max(1, org.liveLength // 2)  # Skraca życie o połowę, minimum 1
            self.__plague_turns_remaining -= 1
            if self.__plague_turns_remaining <= 0:
                self.__plague_active = False
                self.__turns_since_last_plague = 0
        else:
            self.__turns_since_last_plague += 1

        actions = []

        for org in self.organisms:
            if self.positionOnBoard(org.position):
                actions = org.move()
                for a in actions:
                    self.makeMove(a)
                actions = []
                if self.positionOnBoard(org.position):
                    actions = org.action()
                    for a in actions:
                        self.makeMove(a)
                    actions = []

        self.organisms = [o for o in self.organisms if self.positionOnBoard(o.position)]
        for o in self.organisms:
            o.liveLength -= 1
            o.power += 1
            if o.liveLength < 1:
                print(f"{o.__class__.__name__}: died of old age at: {o.position}")
        self.organisms = [o for o in self.organisms if o.liveLength > 0]

        self.newOrganisms = [o for o in self.newOrganisms if self.positionOnBoard(o.position)]
        self.organisms.extend(self.newOrganisms)
        self.organisms.sort(key=lambda o: o.initiative, reverse=True)
        self.newOrganisms = []

        self.turn += 1

    def add_custom_organism(self, organism_type, position):
        '''Dodaje nowy organizm wybranego typu na określoną pozycję'''
        if organism_type in self.__available_organisms:
            if self.getOrganismFromPosition(position) is None:
                new_org = self.__available_organisms[organism_type](
                    position=position,
                    world=self
                )
                return self.addOrganism(new_org)
            print("Pozycja jest już zajęta!")
            return False
        print("Nieznany typ organizmu!")
        return False

    def makeMove(self, action):
        '''Wykonuje ruch organizmu na podstawie akcji'''
        print(action)
        if action.action == ActionEnum.A_ADD:
            self.newOrganisms.append(action.organism)
        elif action.action == ActionEnum.A_INCREASEPOWER:
            action.organism.power += action.value
        elif action.action == ActionEnum.A_MOVE:
            action.organism.position = action.position
        elif action.action == ActionEnum.A_REMOVE:
            action.organism.position = Position(xPosition=-1, yPosition=-1)

    def addOrganism(self, newOrganism):
        '''Dodaje nowego organizm do świata, jeśli jego pozycja jest poprawna'''
        newOrgPosition = Position(xPosition=newOrganism.position.x, yPosition=newOrganism.position.y)

        if self.positionOnBoard(newOrgPosition):
            self.organisms.append(newOrganism)
            self.organisms.sort(key=lambda org: org.initiative, reverse=True)
            return True
        return False

    def positionOnBoard(self, position):
        '''Sprawdza, czy dana pozycja znajduje się na planszy'''
        return position.x >= 0 and position.y >= 0 and position.x < self.worldX and position.y < self.worldY

    def getOrganismFromPosition(self, position):
        '''Zwraca organizm znajdujący się na danej pozycji, jeśli taki istnieje'''
        pomOrganism = None

        for org in self.organisms:
            if org.position == position:
                pomOrganism = org
                break
        if pomOrganism is None:
            for org in self.newOrganisms:
                if org.position == position:
                    pomOrganism = org
                    break
        return pomOrganism

    def getNeighboringPositions(self, position):
        '''Zwraca listę sąsiadujących pozycji wokół danej pozycji'''
        result = []
        pomPosition = None

        for y in range(-1, 2):
            for x in range(-1, 2):
                pomPosition = Position(xPosition=position.x + x, yPosition=position.y + y)
                if self.positionOnBoard(pomPosition) and not (y == 0 and x == 0):
                    result.append(pomPosition)
        return result

    def filterFreePositions(self, fields):
        '''Zwraca listę wolnych pozycji z podanej listy, czyli takich, na których nie ma organizmów'''
        result = []

        for field in fields:
            if self.getOrganismFromPosition(field) is None:
                result.append(field)
        return result

    def filterPositionsWithoutAnimals(self, fields):
        '''Zwraca listę pozycji, na których nie ma zwierząt, czyli tylko rośliny lub puste pola'''
        result = []
        pomOrg = None

        for filed in fields:
            pomOrg = self.getOrganismFromPosition(filed)
            if pomOrg is None or isinstance(pomOrg, Plant):
                result.append(filed)
        return result

    def __str__(self):
        '''Zwraca reprezentację tekstową świata, w tym organizmów i ich pozycji'''
        COLORS = {
            'G': '\033[32m',
            'S': '\033[97m',
            'A': '\033[93m',
            'R': '\033[91m',
            'default': '\033[0m'
        }

        result = f'\nturn: {self.__turn}'
        if self.__plague_active:
            result += f' (PLAGA aktywna przez {self.__plague_turns_remaining} tur)'
        result += '\n\n'


        for wY in range(0, self.worldY):
            for wX in range(0, self.worldX):
                org = self.getOrganismFromPosition(Position(xPosition=wX, yPosition=wY))
                if org:
                    color = COLORS.get(org.sign, COLORS['default'])
                    result += f" {color}{org.sign}{COLORS['default']} "
                else:
                    result += self.separator
            result += f"| {wY % 10}\n"

        result += " " + '  '.join('-' for _ in range(self.worldX)) + '\n'
        result += " "+'  '.join([str(i % 10) for i in range(self.worldX)]) + '\n'
        return result