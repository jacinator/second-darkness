from templates.territories import territory

import mordor, rohan, gondor

from mordor.army import *
from gondor.army import *
from rohan.army import *
from rohan.heroes import eomer

wold = territory(
    name = 'the Wold',
    occupants = rohan,
    neighbours = [
        'Fangorn Forest',
        'East Emnet',
        'Parth Celebrant',
        'the Brown Lands',
    ],
    army = [riders] * 4,
)

east_emnet = territory(
    name = 'East Emnet',
    occupants = rohan,
    neighbours = [
        'West Emnet',
        'the Eastfold',
        'Emyn Muil',
        'Anorien',
    ],
    value = 3,
    army = [rohirrim] * 4 + [riders] * 2,
)

west_emnet = territory(
    name = 'West Emnet',
    occupants = rohan,
    neighbours = [
        'East Emnet',
        'Fangorn Forest',
        'the Westfold',
        'the Eastfold',
        'the Gap of Rohan',
    ],
    value = 3,
    army = [eomer] + [rohirrim] * 4 + [riders],
    recruitment = True,
    city_name = 'Entwade',
    city_level = 1,
)

anorien = territory(
    name = 'Anorien',
    subname = 'the Sun-land',
    occupants = gondor,
    value = 4,
    neighbours = [
        'the Eastfold',
        'East Emnet',
        'Nindalf',
        'North Ithilien',
        'the Fields of Pelennor',
        'Druadan Forest',
    ],
    army = [gondorians] * 4 + [gondorian_archers] * 2 + [ithilien_rangers] * 3,
)

nindalf = territory(
    name = 'Nindalf',
    subname = 'Wetwang',
    occupants = mordor,
    neighbours = [
        'Anorien',
        'Emyn Muil',
        'Noman-lands',
        'the Dead Marshes',
    ],
)

dead_marshes = territory(
    name = 'the Dead Marshes',
    occupants = mordor,
    neighbours = [
        'Nindalf',
        'Noman-lands',
        'Emyn Muil',
        'the East Bight',
    ],
)

noman_lands = territory(
    name = 'Noman-lands',
    occupants = mordor,
    neighbours = [
        'Nindalf',
        'the Dead Marshes',
        'North Ithilien',
        'Udun',
    ],
    army = [uruk] * 5,
)

emyn_muil = territory(
    name = 'Emyn Muil',
    occupants = rohan,
    neighbours = [
        'Nindalf',
        'the Dead Marshes',
        'the Brown Lands',
        'the East Bight',
    ],
)

brown_lands = territory(
    name = 'the Brown Lands',
    occupants = rohan,
    neighbours = [
        'the Wold',
        'Emyn Muil',
        'Dol Guldur',
    ],
)
