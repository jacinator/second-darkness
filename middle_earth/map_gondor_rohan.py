from templates.territories import territory
from functions.strings_digits import idnumber, space

import gondor, rohan, dunland, harad, isengard, mordor

from gondor.army import *
from gondor.heroes import *
from rohan.army import *
from rohan.heroes import *
from dunland.army import *
from harad.army import *
from isengard.army import *
from mordor.army import *

druwaith_iaur = territory(
    name = 'Druwaith Iaur',
    subname = 'Old Pukel-land',
    occupants = dunland,
    neighbours = [
        'Enedwaith',
        'Pinnath Gelin',
        'Ras Morthil Andrast',
        'the Gap of Rohan',
        'Enedwaith',
    ],
    value = 3,
    army = [dunlendings] * 6,
)

anfalas = territory(
    name = 'Anfalas',
    subname = 'Long-shore',
    occupants = gondor,
    value = 2,
    neighbours = [
        'Ras Morthil Andrast',
        'Pinnath Gelin',
    ],
    army = [gondorians] * 2,
)

ras_morthil_andrast = territory(
    name = 'Ras Morthil Andrast',
    occupants = gondor,
    neighbours = [
        'Anfalas',
        'Druwaith Iaur',
    ],
    army = [gondorians] * 2,
)

pinnath_gelin = territory(
    name = 'Pinnath Gelin',
    occupants = gondor,
    value = 2,
    neighbours = [
        'Anfalas',
        'Druwaith Iaur',
        'Lamedon',
    ],
    army = [gondorians] * 3,
)

lamedon = territory(
    name = 'Lamedon',
    occupants = gondor,
    value = 3,
    neighbours = [
        'Pinnath Gelin',
        'Dol Amroth',
        'Lebennin',
    ],
    army = [gondorians] * 4,
    recruitment = True,
    city_name = 'Calembel',
    city_level = 2,
)

dol_amroth = territory(
    name = 'Dol Amroth',
    occupants = gondor,
    neighbours = [
        'Lamedon',
        'Belfalas',
    ],
    army = [gondorians] * 4 + [knights] * 3 + [gondorian_archers] * 2,
    recruitment = True,
    city_name = 'Edhellond',
    city_level = 4,
)

belfalas = territory(
    name = 'Belfalas',
    occupants = gondor,
    neighbours = [
        'Dol Amroth',
        'Dor-en-Ernil',
    ],
    value = 2,
    army = [knights] * 4 + [gondorian_archers] * 2,
)

dor_en_ernil = territory(
    name = 'Dor-en-Ernil',
    subname = 'the Land of the Prince',
    occupants = gondor,
    neighbours = [
        'Lebennin',
        'Belfalas',
    ],
    value = 3,
    army = [gondorians] + [knights] * 3 + [gondorian_archers] * 2,
)

lebennin = territory(
    name = 'Lebennin',
    occupants = gondor,
    neighbours = [
        'Lamedon',
        'Dor-en-Ernil',
        'Harondor',
        'South Ithilien',
    ],
    value = 4,
    army = [gondorians] * 2 + [knights] * 2 + [gondorian_archers] * 4 + [ithilien_rangers] * 2,
    recruitment = True,
    city_name = 'Pelargir',
    city_level = 3,
)

south_ithilien = territory(
    name = 'South Ithilien',
    subname = 'Moon-land',
    occupants = gondor,
    neighbours = [
        'Lebennin',
        'Harondor',
        'the Fields of Pelennor',
    ],
    value = 3,
    army = [ithilien_rangers] * 6 + [gondorians] * 5 + [faramir],
)

pelennor = territory(
    name = 'the Fields of Pelennor',
    subname = 'the Fenced Land',
    occupants = gondor,
    neighbours = [
        'North Ithilien',
        'South Ithilien',
        'Anorien',
    ],
    value = 5,
    recruitment = True,
    city_name = 'Minas Tirith',
    city_level = 5,
    army = [denethor, pippin, boromir, knights] + [gondorians] * 5 + [tower_guard] * 3 + [ithilien_rangers] * 2,
)

harondor = territory(
    name = 'Harondor',
    subname = 'South Gondor',
    occupants = harad,
    neighbours = [
        'Lebennin',
        'South Ithilien',
        'Near Harad',
    ],
    value = 3,
    army = [haradrim] * 4 + [mumak] + [troll_men] * 2,
)

north_ithilien = territory(
    name = 'North Ithilien',
    occupants = mordor,
    neighbours = [
        'Noman-lands',
        'Anorien',
        'the Fields of Pelennor',
        'the Morgul Vale',
    ],
    value = 3,
    army = [nazgul] * 2 + [uruk] * 6 + [troll] * 3,
)

gap_of_rohan = territory(
    name = 'the Gap of Rohan',
    occupants = isengard,
    neighbours = [
        'Enedwaith',
        'Druwaith Iaur',
        'West Emnet',
        'Nan Curunir',
    ],
    value = 2,
    army = [lurtz, warg_riders] + [uruk_hai] * 10,
)

westfold = territory(
    name = 'the Westfold',
    occupants = rohan,
    neighbours = [
        'West Emnet',
    ],
    value = 3,
    army = [merry, theoden, eowyn] + [riders] * 5 + [rohirrim] * 4 + [royal_guard] * 4,
    recruitment = True,
    city_name = 'Edoras',
    city_level = 3,
)

eastfold = territory(
    name = 'the Eastfold',
    occupants = rohan,
    neighbours = [
        'West Emnet',
        'East Emnet',
        'Anorien',
        'Druadan Forest',
    ],
    value = 3,
    army = [rohirrim] * 3 + [riders] * 7,
    recruitment = True,
    city_name = 'Dunharrow',
    city_level = 2,
)
