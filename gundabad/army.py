import gundabad

from templates.units import infantry, heavy, ranged, mounted, hero
from templates.abilities import leadership, fear

snaga = infantry(
    name = 'Gundabad Orcs',
    strength = 200,
    moral = 50,
    faction = gundabad,
    cost = 5,
)

defilers = heavy(
    name = 'Defilers',
    strength = 100,
    moral = 90,
    ability = fear,
    faction = gundabad,
)

gundabad_archers = ranged(
    name = 'Gundabad Archers',
    strength = 140,
    moral = 50,
    faction = gundabad,
)

wargs = mounted(
    name = 'Wargs',
    strength = 100,
    moral = 50,
    faction = gundabad,
)

bolg = hero(
    name = 'Bolg',
    strength = 160,
    moral = 100,
    ability = leadership,
    faction = gundabad,
    ability_factor = 30,
)

azog = hero(
    name = 'Azog',
    strength = 160,
    moral = 100,
    ability = fear,
    faction = gundabad,
    ability_factor = 20,
)
