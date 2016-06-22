import mordor

from templates.units import creature, infantry, heavy, ranged, hero
from templates.abilities import fear, black_breath

uruk = infantry(
    name = 'Mordor Uruks',
    strength = 220,
    moral = 50,
    faction = mordor,
    cost = 5,
)

troll = creature(
    name = 'Troll',
    strength = 100,
    docility = 40,
    faction = mordor,
)

trolls = troll

olog_hai = heavy(
    name = 'Olog hai',
    strength = 60,
    moral = 60,
    faction = mordor,
)

orc_archers = ranged(
    name = 'Mordor Archers',
    strength = 200,
    moral = 50,
    faction = mordor,
    level = 1,
)

nazgul = hero(
    name = 'Nazgul',
    strength = 200,
    moral = 100,
    ability = black_breath,
    faction = mordor,
    ability_factor = 40,
)

angmar = hero(
    name = 'Angmar',
    strength = 200,
    moral = 100,
    ability = fear,
    faction = mordor,
    ability_factor = 50,
)
