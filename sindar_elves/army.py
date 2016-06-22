import sindar_elves

from templates.units import infantry, heavy, ranged, mounted, hero
from templates.abilities import silence, charge, vision, resources

lorien_infantry = infantry(
    name = 'Lorien Infantry',
    strength = 80,
    moral = 100,
    faction = sindar_elves,
)

lorien_spearmen = heavy(
    name = 'Galadrim',
    strength = 60,
    moral = 100,
    faction = sindar_elves,
)

lorien_archers = ranged(
    name = 'Galadrim Archers',
    strength = 100,
    moral = 100,
    ability = silence,
    faction = sindar_elves,
)

sindar_lancers = mounted(
    name = 'Sindar Lancers',
    strength = 50,
    moral = 100,
    faction = sindar_elves,
)

galadriel = hero(
    name = 'Galadriel',
    strength = 120,
    moral = 100,
    ability = vision,
    faction = sindar_elves,
    ability_factor = 40,
)

celeborn = hero(
    name = 'Celeborn',
    strength = 100,
    moral = 100,
    ability = resources,
    faction = sindar_elves,
    ability_factor = 30,
)
