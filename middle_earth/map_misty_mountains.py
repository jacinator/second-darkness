from templates.territories import territory

import gundabad, high_elves, sindar_elves, dunland, ents, isengard, beornings, eagles

from gundabad.army import *
from high_elves.army import *
from sindar_elves.army import *
from dunland.army import *
from ents.army import *
from isengard.army import *
from beornings.army import *
from eagles.army import *

northern_waste = territory(
    name = 'the Northern Waste',
    occupants = gundabad,
    neighbours = [
        'Carn Dum',
        'Mount Gundabad',
        'Ered Mithrin',
    ],
    value = 2,
    army = [snaga] * 8,
)

mount_gundabad = territory(
    name = 'Mount Gundabad',
    occupants = gundabad,
    neighbours = [
        'Carn Dum',
        'Ered Mithrin',
        'Hithaeglir',
        'the Carrock',
    ],
    value = 4,
    army = [snaga] * 5 + [gundabad_archers] * 3 + [wargs] * 4 + [bolg],
    recruitment = True,
    city_name = 'Framsburg',
    city_level = 4,
)

ered_mithrin = territory(
    name = 'Ered Mithrin',
    occupants = gundabad,
    neighbours = [
        'the Northern Waste',
        'Hithaeglir',
        'Mount Gundabad',
        'the Woodland Realm',
        'the Withered Heath',
    ],
    value = 2,
    subname = 'the Grey Mountains',
    army = [snaga] * 5 + [wargs] * 3,
)

hithaeglir = territory(
    name = 'Hithaeglir',
    occupants = gundabad,
    neighbours = [
        'Ered Mithrin',
        'Carn Dum',
        'the Ettenmoors',
        'Rhudaur',
        'the Carrock',
        'Moria',
        'Rivendell',
        'Mount Gundabad',
    ],
    subname = 'the Misty Mountains',
    value = 7,
    army = [wargs] * 3 + [defilers] * 2 + [gundabad_archers] * 2,
    recruitment = True,
    city_name = 'Goblin-town',
    city_level = 2,
)

rhudaur = territory(
    name = 'Rhudaur',
    occupants = gundabad,
    value = 2,
    neighbours  =[
        'the Ettenmoors',
        'Hithaeglir',
        'Rivendell',
        'the Weather Hills',
    ],
    army = [wargs] * 2 + [snaga] * 3,
)

rivendell = territory(
    name = 'Rivendell',
    subname = 'Imladris',
    value = 9,
    occupants = high_elves,
    neighbours = [
        'Rhudaur',
        'Moria',
        'Eregion',
        'Hithaeglir',
        'the South Downs',
    ],
    army = [noldorim] * 4 + [gondolin_knights] * 5 + [elrond],
    recruitment = True,
    city_name = 'Imladris',
    city_level = 4,
)

carrock = territory(
    name = 'the Carrock',
    value = 8,
    occupants = beornings,
    army = [skin_changers] * 3 + [beorning_archers] * 2 + [beorn],
    recruitment = True,
    city_name = 'the Carrock',
    city_level = 1,
    neighbours = [
        'Mount Gundabad',
        'Hithaeglir',
        'Loeg Ningloron',
        'the Woodland Realm',
        'Mirkwood',
    ],
)

loeg_ningloron = territory(
    name = 'Loeg Ningloron',
    subname = 'the Gladden Fields',
    value = 3,
    occupants = beornings,
    neighbours = [
        'the Carrock',
        'Moria',
        'Lorien',
        'Dol Guldur',
        'Mirkwood',
    ],
    army = [skin_changers] * 2 + [beorning_infantry] * 2,
)

eregion = territory(
    name = 'Eregion',
    subname = 'Hollin',
    value = 2,
    occupants = dunland,
    neighbours = [
        'Rivendell',
        'Enedwaith',
        'Moria',
        'the South Downs',
    ],
)

moria = territory(
    name = 'Moria',
    subname = 'Khazad Dum',
    value = 12,
    occupants = gundabad,
    recruitment = True,
    city_name = 'Dwarrowdelf',
    city_level = 4,
    neighbours = [
        'Eregion',
        'Hithaeglir',
        'Loeg Ningloron',
        'Lorien',
        'Methedras',
    ],
    army = [gundabad_archers] * 4 + [defilers] * 4 + [snaga] * 3 + [azog],
)

enedwaith = territory(
    name =  'Enedwaith',
    subname = 'Dunland',
    value = 6,
    occupants = dunland,
    recruitment = True,
    city_name = 'Tharbad',
    city_level = 2,
    neighbours = [
        'Eregion',
        'Isengard',
        'Methedras',
        'the South Downs',
        'Druwaith Iaur',
        'Sarn Ford',
    ],
    army = [dunlendings] * 5 + [dunland_archers] * 3,
)

lorien = territory(
    name = 'Lorien',
    subname = 'Lothlorien',
    value = 10,
    occupants = sindar_elves,
    recruitment = True,
    city_name = 'Caras Galadon',
    city_level = 7,
    neighbours = [
        'Parth Celebrant',
        'Loeg Ningloron',
        'Moria',
        'Dol Guldur',
    ],
    army = [lorien_spearmen] * 4 + [lorien_archers] * 5 + [galadriel, celeborn],
)

parth_celebrant = territory(
    name = 'Parth Celebrant',
    subname = 'the Field of Celebrant',
    value = 5,
    occupants = sindar_elves,
    neighbours = [
        'Lorien',
        'Fangorn Forest',
        'Methedras',
        'Dol Guldur',
        'the Wold',
    ],
    army = [sindar_lancers] * 3 + [lorien_infantry] * 4,
)

fangorn = territory(
    name = 'Fangorn Forest',
    subname = 'the Entwood',
    value = 10,
    occupants = ents,
    neighbours = [
        'Parth Celebrant',
        'Methedras',
        'Nan Curunir',
        'the Wold',
    ],
    army = [onodrim] * 3 + [huorns, treebeard],
    recruitment = True,
    city_name = 'Wellinghall',
    city_level = 2,
)

eyrie = territory(
    name = 'the Eagles Eyrie',
    value = 10,
    occupants = eagles,
    neighbours = [
        'Hithaeglir',
        'the Carrock',
    ],
    army = [eagle] * 5 + [thorondor],
    recruitment = True,
    city_name = 'the Eagles Eyrie',
    city_level = 2,
)

methedras = territory(
    name = 'Methedras',
    subname = 'the Last Peak',
    value = 2,
    occupants = isengard,
    neighbours = [
        'Fangorn Forest',
        'Nan Curunir',
        'Enedwaith',
        'Parth Celebrant',
    ],
    army = [warg_riders] * 4 + [orcs] * 4,
)

nan_curunir = territory(
    name = 'Nan Curunir',
    subname = "the Wizard's Vale",
    value = 8,
    occupants = isengard,
    neighbours = [
        'Enedwaith',
        'Fangorn Forest',
        'Methedras',
        'the Gap of Rohan',
    ],
    army = [uruk_hai] * 10 + [uruk_archers] * 5 + [warg_riders] * 3 + [orcs] * 3 + [saruman],
    recruitment = True,
    city_name = 'Isengard',
    city_level = 5,
)
