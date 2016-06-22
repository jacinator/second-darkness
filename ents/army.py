import ents

from templates.units import creature, heavy, hero
from templates.abilities import invulnerability

huorns = creature(
    name = 'Huorns',
    strength = 50,
    docility = 100,
    ability = invulnerability,
    faction = ents,
)
onodrim = heavy(
    name = 'Ents',
    strength = 30,
    moral = 100,
    ability = invulnerability,
    faction = ents,
)

treebeard = hero(
    name = 'Treebeard',
    moral = 100,
    ability = invulnerability,
    strength = 90,
    faction = ents,
    ability_factor = 50,
)
