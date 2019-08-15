from random import choices, random

from functions.battles import battle

def _normalize_weights(weights):
    diff = 1 - sorted(weights)[0]
    return [w + diff for w in weights]

def _computer_choose(choices, get_weight):
    weights = [get_weight(c) for c in choices]
    return choices(choices, _normalize_weights(weights))[0]

def choose_friendly_neighbor(nation, region):
    return _computer_choose(
        list(region.get_friendly_neighbors()),
        lambda n: sum(region.army.values()) / max(1, sum(n.army.values())),
    )

def choose_hostile_neighbor(nation, region):
    return _computer_choose(
        list(region.get_hostile_neighbors()),
        lambda n: sum(n.army.values()) / max(1, sum(region.army.values())),
    )

def choose_recruit_region(nation):
    return _computer_choose(
        [r for r in nation.get_regions() if r.developed],
        lambda r: r.developed / sum(r.army.values()),
    )

def choose_recruitable_unit(nation, region):
    return _computer_choose(
        [u for u in nation.army if u.developed <= region.developed and u.cost <= nation.resources],
        lambda u: (u.defense + u.offense) / u.cost,
    )

def choose_strong_region(nation):
    return _computer_choose(
        list(nation.get_regions()),
        lambda r: sum(r.army.values()) / len(tuple(r.get_hostile_neighbors())),
    )

def run_computer(nation, turns=4):
    fails = {"a": False, "m": False, "r": False}

    while turns > 0 and not all(fails.values()):
        if random() > 0.66:
            region = choose_strong_region(nation)
            against = choose_hostile_neighbor(nation, region)

            battle(nation, region, against)

        if random() > 0.66:
            region = choose_strong_region(nation)
            to = choose_friendly_neighbor(nation, region)

            region.move_units(nation, to)

        if random() > 0.66:
            region = choose_recruit_region(nation)
            unit = choose_recruitable_unit(nation, region)

            nation.resources -= unit.cost
            region.add_units({unit: 1})
