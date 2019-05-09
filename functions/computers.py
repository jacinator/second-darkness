import random

from templates import regions


def choose_neighbor(nation, region):
    def _compare(neighbor):
        return region.get_strength() / neighbor.get_strength()
    neighbors = list(filter(
        lambda x: x.occupants == nation,
        region.get_neighbors(),
    ))
    weights = list(map(_compare, neighbors))
    return random.choices(neighbors, weights)[0]

def choose_enemy(nation, region):
    def _compare(neighbor):
        return neighbor.get_strength() / region.get_strength()
    neighbors = list(filter(
        lambda x: x.occupants != nation,
        region.get_neighbors(),
    ))
    weights = list(map(_compare, neighbors))
    return random.choices(neighbors, weights)[0]
