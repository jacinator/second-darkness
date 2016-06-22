import halflings

from templates.units import hero
from templates.abilities import courage, command, leadership, invulnerability

frodo = hero(
    name = 'Frodo',
    strength = 100,
    moral = 90,
    ability = command,
    faction = halflings,
    ability_factor = 20,
)

sam = hero(
    name = 'Sam',
    strength = 110,
    moral = 100,
    ability = courage,
    faction = halflings,
    ability_factor = 25,
)

cotton = hero(
    name = 'Farmer Cotton',
    strength = 120,
    moral = 100,
    ability = leadership,
    faction = halflings,
    ability_factor = 15,
)

bombadil = hero(
    name = 'Tom Bombadil',
    strength = 150,
    moral = 100,
    ability = invulnerability,
    faction = halflings,
    ability_factor = 50,
)