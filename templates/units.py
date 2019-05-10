import random


class Unit(object):

    def __init__(self, name, nations, cost, offense, defense):
        for nation in nations:
            nation.army.append(self)

        self.name = name
        self.cost = cost
        self.nations = nations
        self.offense = offense
        self.defense = defense

    def __str__(self):
        return self.name

    def get_damage(self, base):
        return random.randint(1, 6) <= base

    def get_defense_damage(self):
        return self.get_damage(self.defense)

    def get_offense_damage(self):
        return self.get_damage(self.offense)


class CavalryUnit(Unit):
    developed = 4

    def __init__(self, name, nations):
        super().__init__(name, nations, cost=18, offense=4, defense=2)


class MilitiaUnit(Unit):
    developed = 1

    def __init__(self, name, nations):
        super().__init__(name, nations, cost=10, offense=1, defense=2)


class MissileUnit(Unit):
    developed = 3

    def __init__(self, name, nations):
        super().__init__(name, nations, cost=18, offense=2, defense=4)


class MonsterUnit(Unit):
    developed = 5

    def __init__(self, name, nations):
        super().__init__(name, nations, cost=10, offense=2, defense=1)


class RegularUnit(Unit):
    developed = 2

    def __init__(self, name, nations):
        super().__init__(name, nations, cost=14, offense=3, defense=3)
