import beornings

from templates.units import infantry, heavy, ranged, hero
from templates.abilities import rage

beorning_infantry = infantry(
    name = 'Beornings',
    strength = 120,
    moral = 90,
    faction = beornings,
)

skin_changers = heavy(
    name = 'Bear Men',
    strength = 90,
    moral = 90,
    ability = rage,
    faction = beornings,
)

beorning_archers = ranged(
    name = 'Beorning Archers',
    strength = 90,
    moral = 90,
    faction = beornings,
)

beorn = hero(
    name = 'Beorn',
    strength = 120,
    moral = 100,
    ability = rage,
    faction = beornings,
    ability_factor = 30,
)
