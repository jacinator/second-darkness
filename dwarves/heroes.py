import dwarves

from templates.units import hero
from templates.abilities import leadership, courage, burglar, rage, command, accuracy, resources

dain = hero(
    name = 'Dain',
    strength = 100,
    moral = 90,
    ability = command,
    faction = dwarves,
    ability_factor = 30,
)

gimli = hero(
    name = 'Gimli',
    strength = 110,
    moral = 100,
    ability = courage,
    faction = dwarves,
    ability_factor = 25,
)

bilbo = hero(
    name = 'Bilbo',
    strength = 70,
    moral = 100,
    ability = burglar,
    faction = dwarves,
    ability_factor = 20,
)

thorin = hero(
    name = 'Thorin',
    strength = 140,
    moral = 100,
    ability = leadership,
    faction = dwarves,
    ability_factor = 40,
)

dwalin = hero(
    name = 'Dwalin',
    strength = 170,
    moral = 90,
    ability = rage,
    faction = dwarves,
    ability_factor = 20,
)

balin = hero(
    name = 'Balin',
    strength = 90,
    moral = 100,
    ability = resources,
    faction = dwarves,
    ability_factor = 15,
)

fili = hero(
    name = 'Fili',
    strength = 70,
    moral = 100,
    ability = courage,
    faction = dwarves,
)

kili = hero(
    name = 'Kili',
    strength = 70,
    moral = 100,
    ability = leadership,
    faction = dwarves,
)

dori = hero(
    name = 'Dori',
    strength = 70,
    moral = 100,
    ability = courage,
    faction = dwarves,
)

ori = hero(
    name = 'Ori',
    strength = 70,
    moral = 100,
    ability = accuracy,
    faction = dwarves,
)

nori = hero(
    name = 'Nori',
    strength = 70,
    moral = 100,
    ability = courage,
    faction = dwarves,
)

oin = hero(
    name = 'Oin',
    strength = 70,
    moral = 100,
    ability = resources,
    faction = dwarves,
)

gloin = hero(
    name = 'Gloin',
    strength = 70,
    moral = 100,
    ability = resources,
    faction = dwarves,
)

bifur = hero(
    name = 'Bifur',
    strength = 70,
    moral = 100,
    ability = resources,
    faction = dwarves,
)

bofur = hero(
    name = 'Bofur',
    strength = 70,
    moral = 100,
    ability = courage,
    faction = dwarves,
)

bombur = hero(
    name = 'Bombur',
    strength = 70,
    moral = 100,
    ability = rage,
    faction = dwarves,
    ability_factor = 15,
)

bard = hero(
    name = 'Bard the Bowman',
    strength = 120,
    moral = 100,
    ability = accuracy,
    faction = dwarves,
    ability_factor = 15,
)
