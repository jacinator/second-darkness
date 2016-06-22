import dwarves

from templates.units import infantry, heavy, ranged
from templates.abilities import courage, fire_arrows

dwarven_spearmen = infantry(
    name = 'Dwarven Spearmen',
    strength = 120,
    moral = 90,
    faction = dwarves,
)

dwarven_veterans = heavy(
    name = 'Dwarven Veterans',
    strength = 70,
    moral = 100,
    faction = dwarves,
    cost = 30,
)

dwarven_archers = ranged(
    name = 'Dwarven Archers',
    strength = 90,
    moral = 90,
    ability = fire_arrows,
    faction = dwarves,
)

watchmen = heavy(
    name = 'Dale Watchmen',
    strength = 30,
    moral = 100,
    ability = courage,
    faction = dwarves,
    cost = 30,
)

dragon_veterans = ranged(
    name = 'Dragon Veterans',
    strength = 90,
    moral = 100,
    ability = fire_arrows,
    faction = dwarves,
    cost = 40,
)
