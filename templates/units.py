from .abilities import *
from functions import strings_digits

attack_abilities = (
    charge,
    fire_arrows,
    rage,
    fear,
    accuracy,
)

defense_abilities = (
    courage,
    invulnerability,
    black_breath,
)

class infantry(object):
    def __init__(self, name, strength, moral, faction, ability = None, cost = 10):
        self.name = name
        self.strength = strength
        self.moral = moral
        self.attack = self.strength + self.moral
        self.defense = self.strength + self.moral + 50
        self.ability = ability
        self.faction = faction
        self.cost = cost
        self.level = 1
        self.max_strength = strength
        self.broken = False
    
    def review(self):
        if self.strength <= strings_digits.EvenDivide(self.max_strength, 5):
            self.broken = True
        elif self.moral <= 15:
            self.broken = True
    
class heavy(object):
    def __init__(self, name, strength, moral, faction, ability = courage, cost = 20, level = 3):
        self.name = name
        self.strength = strength
        self.moral = moral
        self.attack = self.strength + self.moral + 50
        self.defense = self.strength + self.moral + 150
        self.ability = ability
        self.faction = faction
        self.cost = cost
        self.level = level
        self.max_strength = strength
        self.broken = False
    
    def review(self):
        if self.strength <= strings_digits.EvenDivide(self.max_strength, 10):
            self.broken = True
        elif self.moral <= 10:
            self.broken = True
    
class ranged(object):
    def __init__(self, name, strength, moral, faction, ability = None, cost = 20, level = 2):
        self.name = name
        self.strength = strength
        self.moral = moral
        self.attack = self.strength + self.moral + 150
        self.defense = self.strength + self.moral + 50
        self.ability = ability
        self.faction = faction
        self.cost = cost
        self.level = level
        self.max_strength = strength
        self.broken = False
    
    def review(self):
        if self.strength <= strings_digits.EvenDivide(self.max_strength, 5):
            self.broken = True
        elif self.moral <= 20:
            self.broken = True
    
class mounted(object):
    def __init__(self, name, strength, moral, faction, ability = charge, cost = 30, level = 3):
        self.name = name
        self.strength = strength
        self.moral = moral
        self.attack = self.strength + self.moral + 200
        self.defense = self.strength + self.moral + 50
        self.ability = ability
        self.faction = faction
        self.cost = cost
        self.level = level
        self.max_strength = strength
        self.broken = False
    
    def review(self):
        if self.strength <= strings_digits.EvenDivide(self.max_strength, 4):
            self.broken = True
        elif self.moral <= 15:
            self.broken = True

class creature(object):
    def __init__(self, name, strength, docility, faction, ability = charge, cost = 50, level = 4):
        self.name = name
        self.strength = strength
        self.docility = docility
        self.attack = self.strength + self.docility + 300
        self.defense = self.strength + self.docility + 150
        self.ability = ability
        self.faction = faction
        self.cost = cost
        self.level = level
        self.max_strength = strength
        self.broken = False
    
    def review(self):
        if self.strength <= strings_digits.EvenDivide(self.max_strength, 4):
            self.broken = True
        elif self.docility <= 25:
            self.broken = True
    
class hero(object):
    def __init__(self, name, strength, moral, faction, ability, ability_factor = 10):
        self.name = name
        self.strength = strength
        self.moral = moral
        self.attack = self.strength + self.moral + 400
        self.defense = self.strength + self.moral + 200
        self.ability = ability
        self.ability_active = False
        self.faction = faction
        self.max_strength = strength
        self.broken = False
        self.level = 5
        self.ability_effect = None
        self.ability_factor = ability_factor
        if self.ability in attack_abilities:
            self.ability_effect = self.attack
        elif self.ability in defense_abilities:
            self.ability_effect = self.defense
    
    def review(self):
        if self.strength <= strings_digits.EvenDivide(self.max_strength, 5):
            self.broken = True
        elif self.moral <= 5:
            self.broken = True
    
    def toggle_ability(self):
        if self.ability_active == False:
            self.ability.activate(self)
        else:
            self.ability.deactivate(self)
    