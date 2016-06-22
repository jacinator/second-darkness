from random import choice, randint
from templates.units import hero, defense_abilities
from functions.strings_digits import EvenDivide, LengthManager

class battle(object):
    def __init__(self, aggressor, defender, current_faction, army = None):
        self.aggressor = aggressor
        self.defender = defender
        if army == None:
            self.army = aggressor.army
            self.StorageAttackArmy = aggressor.army
        else:
            self.army = army
            self.StorageAttackArmy = army
        self.defense = defender.army + defender.allies
        self.StorageDefenseArmy = defender.army + defender.allies
        self.DefenseCasualties = []
        self.AssaultCasualties = []
        self.current_faction = current_faction
    
    def fight(self):
        self.DefenseCasualties = []
        self.AssaultCasualties = []
        try:
            for unit in self.StorageAttackArmy:
                try:
                    Enemy = choice(list(self.defense))
                except IndexError:
                    self.defender.occupants = self.aggressor.occupants
                    self.aggressor.move(self.defender, self.aggressor)
                    return 'conquered'
                roll = randint(1, (unit.attack * 2))
                if roll <= unit.attack:
                    if type(Enemy) == hero and Enemy.ability in defense_abilities and Enemy.ability_active == False:
                        Enemy.toggle_ability()
                    Enemy.strength -= EvenDivide(roll, 8)
                    try:
                        Enemy.moral -= EvenDivide(roll, 8)
                    except AttributeError:
                        Enemy.docility -= EvenDivide(roll, 6)
                    try:
                        unit.moral += EvenDivide(roll, 8)
                    except AttributeError:
                        unit.docility += EvenDivide(roll, 6)
                    
                    Enemy.review()
                    if Enemy.broken == True:
                        self.DefenseCasualties.append(Enemy)
                        self.defense.remove(Enemy)
        except RuntimeError:
            pass
        
        try:
            for unit in self.StorageDefenseArmy:
                try:
                    Enemy = choice(list(self.army))
                except IndexError:
                    return 'repulsed'
                roll = randint(1, (unit.attack * 2))
                if roll <= unit.attack:
                    if type(Enemy) == hero and Enemy.ability in defense_abilities and Enemy.ability_active == False:
                        Enemy.toggle_ability()
                    Enemy.strength -= EvenDivide(roll, 8)
                    try:
                        Enemy.moral -= EvenDivide(roll, 8)
                    except AttributeError:
                        Enemy.docility -= EvenDivide(roll, 6)
                    try:
                        unit.moral += EvenDivide(roll, 8)
                    except AttributeError:
                        unit.docility += EvenDivide(roll, 6)
                    
                    Enemy.review()
                    if Enemy.broken == True:
                        self.AssaultCasualties.append(Enemy)
                        self.army.remove(Enemy)
        except RuntimeError:
            pass
        
        if self.defense == []:
            self.defender.occupants = self.current_faction
            self.aggressor.move(self.defender, self.current_faction)
            return 'conquered'
        else:
            return 'repulsed'
    
    def stats(self):
        dead = {}
        killed = []
        if self.AssaultCasualties != []:
            for unit in self.AssaultCasualties:
                try:
                    dead[LengthManager(unit.name, 15)] += 1
                except KeyError:
                    dead[LengthManager(unit.name, 15)] = 1
        if self.DefenseCasualties != []:
            for unit in self.DefenseCasualties:
                try:
                    dead[LengthManager(unit.name, 15)] += 1
                except KeyError:
                    dead[LengthManager(unit.name, 15)] = 1
        if dead != {}:
            print(' '.join(list(dead.keys())))
            for integer in dead.keys():
                killed.append(LengthManager('killed', 15))
                dead[integer] = LengthManager(str(dead[integer]), 15)
            print(' '.join(killed))
            print(' '.join(list(dead.values())))
