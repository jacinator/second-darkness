from .army import *
from .heroes import *
from lists_dictionaries.faction_names import GondorName, DunedainName, DwarvesName, HalflingsName, HighElvesName, RohanName

name = GondorName
cash = 0
subname = 'Westernesse'
AI = True

units = {
    gondorians: 32,
    knights: 14,
    ithilien_rangers: 13,
    tower_guard: 3,
    gondorian_archers: 8,
}

heroes = (
    boromir,
    denethor,
    faramir,
    pippin,
)

allies = [
    DunedainName,
    DwarvesName,
    HalflingsName,
    HighElvesName,
    RohanName,
]
