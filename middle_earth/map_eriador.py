from templates.territories import territory

import high_elves, dunedain, halflings, gundabad, dwarves

from dwarves.army import *
from high_elves.army import *
from dunedain.army import *
from halflings.army import *
from halflings.heroes import *
from gundabad.army import *

from dunedain.heroes import *

harlindon = territory(
    name = 'Harlindon',
    subname = 'South Lindon',
    occupants = high_elves,
    neighbours = [
        'Ered Luin',
    ],
    army = [noldorim] * 2,
)

forlindon = territory(
    name = 'Forlindon',
    occupants = high_elves,
    subname = 'North Lindon',
    neighbours = [
      'Ered Luin',
    ],
    army = [noldorim] * 2,
)

ered_luin = territory(
    name = 'Ered Luin',
    occupants = dwarves,
    neighbours = [
        'Harlindon',
        'Forlindon',
        'Mithlond',
        'Forochel',
        'Emyn Beraid',
        'Sarn Ford',
    ],
    value = 5,
    subname = 'the Blue Mountains',
    army = [dwarven_spearmen] * 5 + [dwarven_archers] * 4,
)

mithlond = territory(
    name = 'Mithlond',
    occupants = high_elves,
    neighbours = [
        'Ered Luin',
        'Emyn Beraid',
        'Forochel',
        'Emyn Uial',
    ],
    value = 8,
    subname = 'the Grey Havens',
    army = [noldorim] * 2 + [mithlond_sentries] * 5 + [gondolin_knights] * 3 + [cirdan],
    recruitment = True,
    city_name = 'the Grey Havens',
    city_level = 4,
)

emyn_beraid = territory(
    name = 'Emyn Beraid',
    occupants = high_elves,
    neighbours = [
        'Mithlond',
        'Ered Luin',
        'the Shire',
    ],
    value = 2,
    subname = 'the Tower Hills',
    army = [mithlond_sentries] * 3,
)

shire = territory(
    name = 'the Shire',
    occupants = halflings,
    neighbours = [
        'Emyn Beraid',
        'Emyn Uial',
        'the North Downs',
        'Bree-land',
        'Sarn Ford',
        'the Barrow-Downs',
    ],
    value = 10,
    army = [hobbits] * 6 + [tooks] * 3 + [hobbit_archers] * 3 + [frodo, sam, cotton],
    recruitment = True,
    city_name = 'Hobbiton',
    city_level = 2,
)

sarn_ford = territory(
    name = 'Sarn Ford',
    occupants = dunedain,
    neighbours = [
        'the Shire',
        'Ered Luin',
        'the South Downs',
        'Enedwaith',
    ],
    army = [arnor_rangers] * 3 + [rangers, elledan],
)

barrow_downs = territory(
    name = 'the Barrow-Downs',
    occupants = halflings,
    neighbours = [
        'the Shire',
        'Bree-land',
        'the South Downs',
    ],
    army = [bombadil],
)

bree_land = territory(
    name = 'Bree-land',
    occupants = halflings,
    neighbours = [
        'the Shire',
        'the North Downs',
        'the South Downs',
        'the Barrow-Downs',
        'the Weather Hills',
    ],
    value = 5,
    army = [hobbits] * 3,
    recruitment = True,
    city_name = 'Bree',
    city_level = 1,
)

weather_hills = territory(
    name = 'the Weather Hills',
    occupants = dunedain,
    neighbours = [
        'Bree-land',
        'the South Downs',
        'the North Downs',
        'the Ettenmoors',
        'Rhudaur',
    ],
    value = 3,
    army = [arnor_rangers] * 3 + [rangers, aragorn],
)

south_downs = territory(
    name = 'the South Downs',
    occupants = dunedain,
    neighbours = [
        'Sarn Ford',
        'the Barrow-Downs',
        'the Weather Hills',
        'Bree-land',
        'Rivendell',
        'Enedwaith',
        'Eregion',
    ],
    army = [arnor_rangers] * 3 + [rangers],
)

north_downs = territory(
    name = 'the North Downs',
    occupants = dunedain,
    neighbours = [
        'the Shire',
        'the Weather Hills',
        'the Ettenmoors',
        'Emyn Uial',
        'Carn Dum',
    ],
    army = [arnor_rangers] * 3 + [rangers] + [mounted_dunedain] * 2,
    recruitment = True,
    city_name = 'Fornost',
    city_level = 3,
)

emyn_uial = territory(
    name = 'Emyn Uial',
    occupants = dunedain,
    neighbours = [
        'Mithlond',
        'the Shire',
        'the North Downs',
    ],
    subname = 'the Hills of Evendim',
    army = [arnor_rangers] * 3 + [rangers, elrohir],
)

carn_dum = territory(
    name = 'Carn Dum',
    occupants = gundabad,
    neighbours = [
        'the Ettenmoors',
        'the North Downs',
        'Mount Gundabad',
        'Hithaeglir',
    ],
    value = 3,
    army = [defilers] * 3 + [snaga] * 2,
    recruitment = True,
    city_name = 'Carn Dum',
    city_level = 3,
)

ettenmoors = territory(
    name = 'the Ettenmoors',
    occupants = gundabad,
    neighbours = [
        'the Weather Hills',
        'the North Downs',
        'Carn Dum',
        'Hithaeglir',
        'Rhudaur',
    ],
    army = [snaga] * 2 + [wargs] * 2,
)
