import halflings

from templates.units import infantry, heavy, ranged
from templates.abilities import silence

hobbits = infantry(
    name = 'Hobbits',
    strength = 200,
    moral = 90,
    ability = silence,
    faction = halflings,
)

tooks = heavy(
    name = 'Tooks',
    strength = 150,
    moral = 90,
    faction = halflings,
    level = 2,
)

hobbit_archers = ranged(
    name = 'Hobbit Archers',
    strength = 200,
    moral = 90,
    ability = silence,
    faction = halflings,
    level = 1,
)
