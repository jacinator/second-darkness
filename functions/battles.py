import random

def get_damage(army, type):
    return sum([sum([getattr(u,'get_{}_damage'.format(type))() for _ in range(c)]) for u, c in army.items()])

def get_casualties(a, b, type):
    casualties = {}

    for _ in range(get_damage(a, type)):
        try:
            unit = random.choice(tuple(b.keys()))
        except IndexError:
            break

        if unit in casualties:
            casualties[unit] += 1
        else:
            casualties[unit] = 1

    return casualties

def battle(nation, offense, defense):
    offense_army = {}

    for unit, count in offense.army.items():
        if nation in unit.nations:
            offense_army[unit] = count

    offense_casualties = get_casualties(defense.army, offense_army, 'defense')
    defense_casualties = get_casualties(offense_army, defense.army, 'offense')

    offense.sub_units(offense_casualties)
    defense.sub_units(defense_casualties)
