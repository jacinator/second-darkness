import rohan

from templates.units import hero
from templates.abilities import leadership, courage, silence

theoden = hero(
    name = 'Theoden',
    strength = 100,
    moral = 100,
    ability = leadership,
    faction = rohan,
    ability_factor = 25,
)

eomer = hero(
    name = 'Eomer',
    strength = 110,
    moral = 100,
    ability = courage,
    faction = rohan,
    ability_factor = 25,
)

eowyn = hero(
    name = 'Eowyn',
    strength = 90,
    moral = 100,
    ability = courage,
    faction = rohan,
    ability_factor = 20,
)

merry = hero(
    name = 'Merry',
    strength = 70,
    moral = 100,
    ability = silence,
    faction = rohan,
    ability_factor = 25,
)
