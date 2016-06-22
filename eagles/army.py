import eagles

from templates.units import creature, hero
from templates.abilities import vision

thorondor = hero(
    name = 'Thorondor',
    strength = 200,
    moral = 100,
    faction = eagles,
    ability = vision,
)

eagle = creature(
    name = 'Eagle',
    strength = 150,
    docility = 100,
    faction = eagles,
    cost = 30,
    level = 2,
)