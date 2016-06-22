import isengard

from templates.units import infantry, heavy, mounted, ranged, hero
from templates.abilities import courage, charge, command, leadership

orcs = infantry(
    name = 'Orcs',
    strength = 200,
    moral = 60,
    faction = isengard,
    cost = 5,
)

uruk_hai = heavy(
    name = 'Uruk Hai',
    strength = 140,
    moral = 90,
    faction = isengard,
    cost = 15,
)

warg_riders = mounted(
    name = 'Warg Riders',
    strength = 100,
    moral = 60,
    faction = isengard,
)

uruk_archers = ranged(
    name = 'Uruk Archers',
    strength = 140,
    moral = 90,
    faction = isengard,
    ability = courage,
)

saruman = hero(
    name = 'Saruman',
    strength = 120,
    moral = 100,
    faction = isengard,
    ability = command,
    ability_factor = 30,
)

lurtz = hero(
    name = 'Lurtz',
    strength = 140,
    moral = 100,
    faction = isengard,
    ability = command,
    ability_factor = 25,
)
