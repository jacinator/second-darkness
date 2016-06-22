import harad

from templates.units import infantry, ranged, heavy, creature
from templates.abilities import rage

haradrim = infantry(
    name = 'Haradrim',
    moral = 80,
    strength = 120,
    faction = harad,
)

southrons = heavy(
    name = 'Southrons',
    moral = 90,
    strength = 120,
    faction = harad,
)

troll_men = heavy(
    name = 'Troll-men',
    strength = 50,
    moral = 80,
    faction = harad,
    ability = rage,
    level = 4,
    cost = 40,
)

harad_archers = ranged(
    name = 'Harad Archers',
    strength = 100,
    moral = 80,
    faction = harad,
)

mumak = creature(
    name = 'Mumak',
    strength = 120,
    docility = 90,
    faction = harad,
)
