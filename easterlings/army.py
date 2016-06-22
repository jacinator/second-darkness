import easterlings

from templates.units import infantry, heavy, ranged, mounted, hero
from templates.abilities import courage, leadership, charge

easterling_infantry = infantry(
    name = 'Easterlings',
    strength = 120,
    moral = 90,
    faction = easterlings,
)

variags = heavy(
    name = 'Variags of Khand',
    strength = 90,
    moral = 100,
    faction = easterlings,
    level = 3,
)

easterling_archers = ranged(
    name = 'Easterling Archers',
    moral = 90,
    strength = 100,
    faction = easterlings,
)

lancers = mounted(
    name = 'Easterling Lancers',
    moral = 90,
    strength = 70,
    faction = easterlings,
)

gothmog = hero(
    name = 'Gothmog',
    strength = 150,
    moral = 100,
    ability = leadership,
    faction = easterlings,
    ability_factor = 25,
)
