import dunedain

from templates.units import hero
from templates.abilities import leadership, courage, vision

aragorn = hero(
    name = 'Aragorn',
    ability = leadership,
    strength = 130,
    moral = 100,
    faction = dunedain,
    ability_factor = 40,
)

elledan = hero(
    name = 'Elledan',
    ability = courage,
    strength = 120,
    moral = 100,
    faction = dunedain,
    ability_factor = 40,
)

elrohir = hero(
    name = 'Elrohir',
    ability = vision,
    strength = 120,
    moral = 100,
    faction = dunedain,
    ability_factor = 30,
)
