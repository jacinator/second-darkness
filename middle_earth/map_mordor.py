from templates.territories import territory
from functions.strings_digits import space, idnumber

import mordor, easterlings, harad, corsairs

from mordor.army import *
from easterlings.army import *
from harad.army import *
from corsairs.army import *

udun = territory(
    name = 'Udun',
    subname = 'Hell',
    occupants = mordor,
    neighbours = [
        'Noman-lands',
        'the Plateau of Gorgoroth',
    ],
    army = [troll] * 2 + [orc_archers] * 5 + [uruk] * 7 + [nazgul],
)

gorgoroth = territory(
    name = 'the Plateau of Gorgoroth',
    occupants = mordor,
    neighbours = [
        'Udun',
        'the Morgul Vale',
        'Nurn',
        'Lithlad',
    ],
    value = 1,
    army = [uruk] * 10 + [orc_archers] * 2,
    recruitment = True,
    city_name = 'Barad Dur',
    city_level = 5,
)

morgul_vale = territory(
    name = 'the Morgul Vale',
    occupants = mordor,
    neighbours = ['North Ithilien', 'the Plateau of Gorgoroth'],
    value = 2,
    army = [angmar] + [nazgul] * 2 + [uruk] * 8 + [orc_archers] * 4,
    recruitment = True,
    city_name = 'Minas Morgul',
    city_level = 4,
)

nurn = territory(
    name = 'Nurn',
    occupants = mordor,
    neighbours = [
        'Lithlad',
        'the Plateau of Gorgoroth',
    ],
    value = 3,
    army = [uruk] * 5 + [orc_archers],
)

lithlad = territory(
    name = 'Lithlad',
    subname = 'the Ash Plain',
    occupants = mordor,
    neighbours = [
        'Khand',
        'Nurn',
        'the Plateau of Gorgoroth',
    ],
    value = 3,
    army = [uruk] * 5,
)

khand = territory(
    name = 'Khand',
    occupants = easterlings,
    neighbours = [
        'Near Harad',
        'Far Harad',
        'Rhun',
        'Lithlad',
    ],
    value = 4,
    army = [gothmog] + [variags] * 6 + [easterling_infantry] * 2,
)

near_harad = territory(
    name = 'Near Harad',
    occupants = harad,
    neighbours = [
        'Khand',
        'Far Harad',
        'Haradwaith',
        'Umbar',
        'Harondor',
    ],
    value = 3,
    army = [haradrim] * 8 + [mumak],
)

far_harad = territory(
    name = 'Far Harad',
    occupants = harad,
    neighbours = [
        'Khand',
        'Near Harad',
        'Haradwaith',
    ],
    value = 3,
    army = [haradrim] * 3 + [mumak] + [southrons] * 4,
)

umbar = territory(
    subname = 'Earnil',
    name = 'Umbar',
    occupants = corsairs,
    neighbours = [
        'Haradwaith',
        'Near Harad',
    ],
    value = 6,
    army = [pirates] * 7 + [corsair_archers] * 4,
    recruitment = True,
    city_name = 'Umbar',
    city_level = 3,
)

haradwaith = territory(
    name = 'Haradwaith',
    occupants = harad,
    neighbours = [
        'Near Harad',
        'Far Harad',
        'Earnil',
    ],
    value = 8,
    army = [southrons] * 3 + [haradrim] * 12 + [harad_archers] * 5 + [mumak] * 3,
    recruitment = True,
    city_name = 'Hyarmendacil',
    city_level = 4,
)
