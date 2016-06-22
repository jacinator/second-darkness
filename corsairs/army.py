import corsairs

from templates.units import infantry, ranged
from templates.abilities import fire_arrows

pirates = infantry(
    name = 'the Corsairs of Umbar',
    strength = 120,
    moral = 90,
    faction = corsairs,
)

corsair_archers = ranged(
    name = 'Corsair Archers',
    strength = 120,
    moral = 90,
    faction = corsairs,
)
