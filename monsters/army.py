import monsters

from templates.units import creature
from templates.abilities import dragon_fire

smaug = creature(
    name = 'Smaug',
    strength = 300,
    docility = 100,
    faction = monsters,
    ability = dragon_fire,
    cost = 100000,
    level = 5,
)