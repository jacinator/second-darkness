import random


class Unit(object):

    def __init__(self, name, nations, offense, defense):
        for nation in nations:
            nation.army.append(self)

        self.name = name
        self.nations = nations
        self.offense = offense
        self.defense = defense

    def get_damage(self, base):
        return random.randint(1, 6) <= base

    def get_defense_damage(self):
        return self.get_damage(self.defense)

    def get_offense_damage(self):
        return self.get_damage(self.offense)


class CavalryUnit(Unit):

    def __init__(self, name, nations):
        super().__init__(name, nations, offense=4, defense=2)


class MilitiaUnit(Unit):

    def __init__(self, name, nations):
        super().__init__(name, nations, offense=1, defense=2)


class MissileUnit(Unit):

    def __init__(self, name, nations):
        super().__init__(name, nations, offense=2, defense=4)


class MonsterUnit(Unit):

    def __init__(self, name, nations):
        super().__init__(name, nations, offense=2, defense=1)


class RegularUnit(Unit):

    def __init__(self, name, nations):
        super().__init__(name, nations, offense=3, defense=3)
