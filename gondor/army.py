import gondor

from templates.units import infantry, heavy, ranged, mounted, hero
from templates.abilities import fire_arrows

gondorians = infantry(
    name = 'Soldiers of Gondor',
    strength = 120,
    moral = 90,
    faction = gondor,
    cost = 8,
)

gondorian_archers = ranged(
    name = 'Gondorian Archers',
    strength = 100,
    moral = 90,
    faction = gondor,
    cost = 10,
    level = 1,
)

tower_guard = heavy(
    name = 'Tower Guard',
    strength = 70,
    moral = 100,
    faction = gondor,
    level = 5,
)

ithilien_rangers = ranged(
    name = 'Ithilien Rangers',
    strength = 90,
    moral = 90,
    ability = fire_arrows,
    faction = gondor,
    level = 3,
)

knights = mounted(
    name = 'Knights of Dol Amroth',
    strength = 70,
    moral = 90,
    faction = gondor,
    level = 4,
)
