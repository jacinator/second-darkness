from templates.territories import territory
from functions.strings_digits import space, idnumber

import gundabad, silvan_elves, dwarves, easterlings, mordor

from gundabad.army import *
from silvan_elves.army import *
from dwarves.army import *
from dwarves.heroes import *
from easterlings.army import *
from mordor.army import *

withered_heath = territory(
    name = 'the Withered Heath',
    value = 2,
    occupants = gundabad,
    neighbours = [
        'Ered Mithrin',
        'the Woodland Realm',
        'the Iron Hills',
        'Erebor',
    ],
    army = [snaga] * 7,
)

erebor = territory(
    name = 'Erebor',
    subname = 'the Lonely Mountain',
    value = 12,
    occupants = dwarves,
    neighbours = [
        'the Withered Heath',
        'the Woodland Realm',
        'the Iron Hills',
        'Esgaroth',
        'Dale',
    ],
    army = [dwarven_veterans] * 8 + [dwarven_spearmen] * 3 + [dain, gimli],
    recruitment = True,
    city_name = 'the Lonely Mountain',
    city_level = 4,
)

dale = territory(
    name = 'Dale',
    occupants = dwarves,
    neighbours = [
        'Erebor',
        'Esgaroth',
    ],
    value = 5,
    army = [watchmen] * 2 + [dragon_veterans] * 3,
)

esgaroth = territory(
    name = 'Esgaroth',
    subname = 'Lake-town',
    occupants = dwarves,
    neighbours = [
        'Erebor',
        'Dale',
        'the Woodland Realm',
        'the Iron Hills',
        'the East Bight',
    ],
    army = [watchmen] * 2 + [dragon_veterans] * 3 + [bard],
    recruitment = True,
    city_name = 'Lake-town',
    city_level = 2,
)

woodland_realm = territory(
    name = 'the Woodland Realm',
    occupants = silvan_elves,
    neighbours = [
        'Emyn-nu-Fuin',
        'Esgaroth',
        'Erebor',
        'the Withered Heath',
        'the Carrock',
        'Ered Mithrin',
        'Mirkwood',
    ],
    army = [mirkwood_guards] * 5 + [silvan_archers] * 5 + [thranduil],
    recruitment = True,
    city_name = "Thranduil's Caverns",
    city_level = 6,
)

emyn_nu_fuin = territory(
    name = 'Emyn-nu-Fuin',
    subname = 'the Mountains of Mirkwood',
    occupants = silvan_elves,
    neighbours = [
        'the Woodland Realm',
        'Mirkwood',
    ],
    value = 3,
    army = [mirkwood_guards] * 3 + [silvan_archers] * 2 + [mirkwood_infantry] * 4 + [legolas],
)

mirkwood = territory(
    name = 'Mirkwood',
    subname = 'Taur-En-Daedelos',
    occupants = mordor,
    value = 4,
    neighbours = [
        'the Carrock',
        'Emyn-nu-Fuin',
        'Loeg Ningloron',
        'Dol Guldur',
        'the East Bight',
        'the Woodland Realm',
    ],
)

dol_guldur = territory(
    name = 'Dol Guldur',
    occupants = mordor,
    value = 7,
    neighbours = [
        'Mirkwood',
        'the East Bight',
        'Loeg Ningloron',
        'Lorien',
        'Parth Celebrant',
        'the Brown Lands',
    ],
    army = [uruk] * 6 + [troll] + [nazgul] * 3 + [orc_archers] * 3,
    recruitment = True,
    city_name = 'Dol Guldur',
    city_level = 5,
)

east_bight = territory(
    name = 'the East Bight',
    subname = 'the Wilderland',
    occupants = easterlings,
    value = 3,
    neighbours = [
        'Dol Guldur',
        'Dorwinion',
        'Esgaroth',
        'Mirkwood',
        'the Dead Marshes',
        'Emyn Muil',
    ],
)

dorwinion = territory(
    name = 'Dorwinion',
    subname = 'the Land of Wines',
    occupants = easterlings,
    value = 5,
    neighbours = [
        'the East Bight',
        'the Iron Hills',
        'Esgaroth',
        'Rhun',
    ],
    army = [easterling_infantry] * 3 + [easterling_archers] * 2,
)

rhun = territory(
    name = 'Rhun',
    occupants = easterlings,
    value = 4,
    neighbours = [
        'Dorwinion',
        'the Iron Hills',
        'Khand',
    ],
    army = [easterling_infantry] * 2 + [easterling_archers],
    recruitment = True,
    city_level = 3,
    city_name = 'Talath Rhunen',
)

iron_hills = territory(
    name = 'the Iron Hills',
    value = 11,
    occupants = dwarves,
    neighbours = [
        'the Withered Heath',
        'Erebor',
        'Esgaroth',
        'Rhun',
        'Dorwinion',
    ],
    recruitment = True,
    city_name = 'Gabilgathod',
    city_level = 3,
    army = [dwarven_spearmen] * 4 + [dwarven_archers] * 3,
)