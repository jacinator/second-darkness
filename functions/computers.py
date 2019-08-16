from random import choices, random

from functions.battles import battle
from functions.strings import capitalize
from templates.nations import Nation

def _normalize_weights(weights):
    diff = 1 - sorted(weights)[0]
    return [w + diff for w in weights]

def _computer_choose(objects, get_weight):
    weights = [get_weight(c) for c in objects]
    return choices(objects, _normalize_weights(weights))[0]

def _is_player(nation):
    return not nation.computer

def _is_region_visible(region):
    return _is_player(region.occupants) or any(_is_player(n.occupants) for n in region.get_neighbors())

def choose_friendly_neighbor(nation, region):
    return _computer_choose(
        list(region.get_friendly_neighbors(nation)),
        lambda n: sum(region.army.values()) / max(1, sum(n.army.values())),
    )

def choose_hostile_neighbor(nation, region):
    return _computer_choose(
        list(region.get_hostile_neighbors(nation)),
        lambda n: sum(n.army.values()) / max(1, sum(region.army.values())),
    )

def choose_recruit_region(nation):
    return _computer_choose(
        [r for r in nation.get_regions() if r.developed],
        lambda r: r.developed / max(1, sum(r.army.values())),
    )

def choose_recruitable_unit(nation, region):
    return _computer_choose(
        [u for u in nation.army if u.developed <= region.developed and u.cost <= nation.resources],
        lambda u: (u.defense + u.offense) / u.cost,
    )

def choose_strong_region(nation):
    return _computer_choose(
        list(nation.get_regions()),
        lambda r: sum(r.army.values()) / max(1, len(tuple(r.get_hostile_neighbors(nation)))),
    )

def run_computer(nation, turns=4):
    fails = {"a": False, "m": False, "r": False}

    while turns > 0 and not all(fails.values()):
        if random() > 0.66:
            try:
                region = choose_strong_region(nation)
                against = choose_hostile_neighbor(nation, region)

                args = (capitalize(nation.name), against.name, region.name,)
                if _is_region_visible(region) and _is_region_visible(against):
                    print("{0} is attacking {1} from {2}".format(*args))
                elif _is_region_visible(region):
                    print("{0} is attacking from {2}".format(*args))
                elif _is_region_visible(against):
                    print("{0} is attacking {1}".format(*args))

                battle(nation, region, against)
                turns -= 2
            except IndexError:
                fails["a"] = True

        if random() > 0.66:
            try:
                region = choose_strong_region(nation)
                to = choose_friendly_neighbor(nation, region)

                args = (capitalize(nation.name), to.name, region.name,)
                if _is_region_visible(region) and _is_region_visible(to):
                    print("{0} is moving to {1} from {2}".format(*args))
                elif _is_region_visible(region):
                    print("{0} is moving from {2}".format(*args))
                elif _is_region_visible(to):
                    print("{0} is moving to {1}".format(*args))

                region.move_units(nation, to)
                turns -= 1
            except IndexError:
                fails["m"] = True

        if random() > 0.66:
            try:
                region = choose_recruit_region(nation)
                unit = choose_recruitable_unit(nation, region)

                if _is_region_visible(region):
                    args = (capitalize(nation.name), unit.name, region.name,)
                    print("{0} is recruiting {1} in {2}".format(*args))

                nation.resources -= unit.cost
                region.add_units({unit: 1})
                turns -= 1
            except IndexError:
                fails["r"] = True
