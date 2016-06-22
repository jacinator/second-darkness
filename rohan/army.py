import rohan

from templates.units import infantry, ranged, mounted
from templates.abilities import charge

rohirrim = infantry(
    name = 'Rohirrim',
    strength = 100,
    moral = 90,
    faction = rohan,
)

royal_guard = mounted(
    name = 'Royal Guard of the Riddermark',
    strength = 120,
    moral = 100,
    faction = rohan,
    cost = 40
)

rohirric_archers = ranged(
    name = 'Rohirric Archers',
    strength = 90,
    moral = 90,
    faction = rohan,
)

riders = mounted(
    name = 'Riders of Rohan',
    strength = 100,
    moral = 100,
    ability = charge,
    faction = rohan,
    level = 1,
    cost = 30,
)
