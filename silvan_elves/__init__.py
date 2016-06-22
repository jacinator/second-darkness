from .army import *
from lists_dictionaries.faction_names import SilvanElvesName, DunedainName, EntsName, HalflingsName, HighElvesName, BeorningsName, SindarElvesName

name = SilvanElvesName
cash = 0
subname = 'Wood Elves'
AI = True

units = {
    mirkwood_infantry: 4,
    mirkwood_guards: 8,
    silvan_archers: 7,
    silvan_lancers: 0,
}

heroes = (legolas, thranduil)

allies = [
    DunedainName,
    EntsName,
    HalflingsName,
    HighElvesName,
    BeorningsName,
    SindarElvesName,
]