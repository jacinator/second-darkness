import silvan_elves

from templates.units import infantry, heavy, ranged, mounted, hero
from templates.abilities import silence, charge

mirkwood_infantry = infantry(
    name = 'Mirkwood Infantry',
    strength = 100,
    moral = 100,
    ability = silence,
    faction = silvan_elves,
)

mirkwood_guards = heavy(
    name = 'Mirkwood Guards',
    strength = 60,
    moral = 100,
    ability = silence,
    faction = silvan_elves,
)

silvan_archers = ranged(
    name = 'Silvan Archers',
    strength = 120,
    moral = 100,
    ability = silence,
    faction = silvan_elves,
)

silvan_lancers = mounted(
    name = 'Silvan Lancers',
    strength = 70,
    moral = 100,
    ability = charge,
    faction = silvan_elves,
)

thranduil = hero(
    name = 'Thranduil',
    strength = 120,
    moral = 100,
    ability = silence,
    faction = silvan_elves,
    ability_factor = 20,
)

legolas = hero(
    name = 'Legolas',
    moral = 100,
    strength = 140,
    ability = silence,
    faction = silvan_elves,
    ability_factor = 20,
)
