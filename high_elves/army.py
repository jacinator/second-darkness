import high_elves

from templates.units import infantry, heavy, ranged, mounted, hero
from templates.abilities import silence, charge, vision, resources, accuracy

noldorim = infantry(
    name = 'Noldor Swordsmen',
    strength = 110,
    moral = 100,
    faction = high_elves,
)

mithlond_sentries = heavy(
    name  = 'Mithlond sentries',
    strength = 60,
    moral = 100,
    ability = silence,
    faction = high_elves,
)

noldor_archers = ranged(
    name = 'Noldor Archers',
    strength = 100,
    moral = 100,
    ability = accuracy,
    faction = high_elves,
    level = 3,
)

gondolin_knights = mounted(
    name = 'Knights of Gondolin',
    strength = 50,
    moral = 100,
    faction = high_elves,
    level = 4,
)

elrond = hero(
    name = 'Elrond',
    strength = 110,
    moral = 100,
    ability = vision,
    faction = high_elves,
    ability_factor = 30,
)

cirdan = hero(
    name = 'Cirdan',
    strength = 80,
    moral = 100,
    ability = resources,
    faction = high_elves,
    ability_factor = 20,
)
