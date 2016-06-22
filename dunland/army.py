import dunland

from templates.units import infantry, ranged
from templates.abilities import rage, fire_arrows

dunlendings = infantry(
    name = 'Dunlendings',
    moral = 90,
    strength = 150,
    ability = rage,
    faction = dunland,
)

dunland_archers = ranged(
    name = 'Dunlending Archers',
    moral = 90,
    ability = fire_arrows,
    strength = 90,
    faction = dunland,
)
