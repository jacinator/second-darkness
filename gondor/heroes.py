import gondor

from templates.units import hero
from templates.abilities import leadership, command, vision, silence

faramir = hero(
    name = 'Faramir',
    strength = 100,
    moral = 100,
    ability = leadership,
    faction = gondor,
    ability_factor = 30,
)

boromir = hero(
    name = 'Boromir',
    strength = 110,
    moral = 90,
    ability = command,
    faction = gondor,
    ability_factor = 35,
)

denethor = hero(
    name = 'Denethor',
    strength = 110,
    moral = 70,
    ability = vision,
    faction = gondor,
    ability_factor = 25,
)

pippin = hero(
    name = 'Pippin',
    strength = 70,
    moral = 100,
    ability = silence,
    faction = gondor,
    ability_factor = 10,
)
