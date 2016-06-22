from .army import *
from lists_dictionaries.faction_names import HighElvesName, DunedainName, DwarvesName, EntsName, GondorName, HalflingsName, SindarElvesName, SilvanElvesName

name = HighElvesName
cash = 0
subname = 'Noldorim'
AI = True

units = {
    noldorim: 10,
    mithlond_sentries: 8,
    noldor_archers: 0,
    gondolin_knights: 8,
}

heroes = (
    elrond,
    cirdan,
)

allies = [
    DunedainName,
    DwarvesName,
    EntsName,
    GondorName,
    HalflingsName,
    SilvanElvesName,
    SindarElvesName,
]
