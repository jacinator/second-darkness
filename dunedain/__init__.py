from .army import *
from .heroes import *
from lists_dictionaries.faction_names import DunedainName, DwarvesName, EntsName, GondorName, HalflingsName, HighElvesName, RohanName, SilvanElvesName, SindarElvesName

name = DunedainName
cash = 1000
AI = True

units = {
    arnor_rangers: 15,
    dunedain_spearmen: 0,
    mounted_dunedain: 2,
    rangers: 5,
}

heroes = (
    aragorn,
    elledan,
    elrohir,
)

allies = [
    DwarvesName,
    EntsName,
    GondorName,
    HalflingsName,
    HighElvesName,
    RohanName,
    SilvanElvesName,
    SindarElvesName,
]