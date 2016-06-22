from .strings_digits import EvenDivide, pluralize, LengthManager
from templates.units import *

from random import choice, randint

def rest(unit, recuperation):
    if unit.movement < unit.movement_cap:
            unit.movement += recuperation
            if unit.movement > unit.movement_cap:
                unit.movement = unit.movement_cap

def GetType(unit):
    if type(unit) == hero:
        return 'hero'
    elif type(unit) == creature:
        return 'creature'
    elif type(unit) == infantry:
        return 'infantry'
    elif type(unit) == heavy:
        return 'heavy'
    elif type(unit) == ranged:
        return 'ranged'
    elif type(unit) == mounted:
        return 'mounted'
    else:
        return None

def PrintUnits(faction, location):
    longest = 0
    for unit in faction.units.keys():
        if len(unit.name) > longest:
            longest = len(unit.name) + 1
    unit_names = ['    NAME:']
    unit_costs = ['    COST:']
    unit_attacks = ['  ATTACK:']
    unit_defenses = [' DEFENSE:']
    current_units = [' CURRENT:']
    for unit in faction.units.keys():
        if unit.level <= location.level:
            unit_names.append(LengthManager(unit.name, longest))
            unit_costs.append(LengthManager('$' + str(unit.cost), longest))
            unit_defenses.append(LengthManager(str(unit.defense), longest))
            unit_attacks.append(LengthManager(str(unit.attack), longest))
            current_units.append(LengthManager(str(faction.units[unit]), longest))
    print(' '.join(unit_names))
    print(' '.join(unit_costs))
    print(' '.join(unit_defenses))
    print(' '.join(unit_attacks))
    print(' '.join(current_units))

def fight(offense, defense, AI = True):
    try:
        for unit in offense.army.keys():
            roll = randint(1, 1000)
            try:
                enemy = choice(list(defense.army.keys()) + list(defense.allies.keys()))
            except IndexError:
                return 'defeated'
            
            if roll <= offense.army[unit].attack:
                moral_factor = EvenDivide(roll, 12)
                strength_factor = EvenDivide(roll, 8)
                try:
                    defense.army[enemy].strength -= strength_factor
                except KeyError:
                    defense.allies[enemy].strength -= strength_factor
                try:
                    defense.army[enemy].moral -= moral_factor
                except KeyError:
                    try:
                        defense.allies[enemy].moral -= moral_factor
                    except AttributeError:
                        defense.army[enemy].docility -= moral_factor
                except AttributeError:
                    defense.army[enemy].docility -= moral_factor
                try:
                    offense.army[unit].moral += moral_factor
                except AttributeError:
                    offense.army[unit].docility += moral_factor
    except RuntimeError:
        return
    
    try:
        defense_casualties = {}
        for unit in list(defense.army.keys()) + list(defense.allies.keys()):
            try:
                defense.army[unit].review()
                if defense.army[unit].broken == True:
                    try:
                        defense_casualties[defense.army[unit].name] += 1
                    except KeyError:
                        defense_casualties[defense.army[unit].name] = 1
                    del defense.army[unit]
            except KeyError:
                defense.allies[unit].review()
                if defense.allies[unit].broken == True:
                    try:
                        defense_casualties[defense.allies[unit].name] += 1
                    except KeyError:
                        defense_casualties[defense.allies[unit].name] = 1
                    del defense.allies[unit]
        
        attack_casualties = {}
        for unit in offense.army:
            offense.army[unit].review()
            if offense.army[unit].broken == True:
                try:
                    attack_casualties[offense.army[unit].name] += 1
                except KeyError:
                    attack_casualties[offense.army[unit].name] = 1
                del offense.army[unit]
    except RuntimeError:
        return
    
    if offense.occupants.AI == False or defense.occupants.AI == False:
        if attack_casualties != {}:
            for unit in attack_casualties.keys():
                print("%d %s killed." % (attack_casualties[unit], unit))
        if defense_casualties != {}:
            for unit in defense_casualties.keys():
                print("%d %s killed." % (defense_casualties[unit], unit))