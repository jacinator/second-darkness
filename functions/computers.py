from random import choices

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
