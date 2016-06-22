import dunedain

from templates.units import infantry, heavy, ranged, mounted
from templates.abilities import silence, leadership, courage, vision, charge

dunedain_spearmen = infantry(
    name = 'Dunedain Spearmen',
    strength = 30,
    moral = 100,
    faction = dunedain,
)

rangers = heavy(
    name = 'Dunedain',
    ability = silence,
    strength = 10,
    moral = 100,
    faction = dunedain,
)

arnor_rangers = ranged(
    name = 'Dunedain Rangers',
    ability = silence,
    strength = 30,
    moral = 100,
    faction = dunedain,
)

mounted_dunedain = mounted(
    name = 'Mounted Dunedain',
    strength = 20,
    moral = 100,
    faction = dunedain,
)
