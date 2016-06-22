from .army import *
from lists_dictionaries.faction_names import EntsName, HalflingsName, HighElvesName, RohanName, SilvanElvesName, SindarElvesName

name = EntsName
cash = 0
subname = 'Onodrim'
AI = True

units = {
    huorns: 1,
    onodrim: 3,
}

heroes = (treebeard)

allies = [
    HalflingsName,
    HighElvesName,
    RohanName,
    SilvanElvesName,
    SindarElvesName,
]