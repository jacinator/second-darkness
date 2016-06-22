from .army import *
from .heroes import *
from lists_dictionaries.faction_names import HalflingsName, BeorningsName, DunedainName, DwarvesName, EntsName, GondorName, HighElvesName, RohanName, SilvanElvesName, SindarElvesName

name = HalflingsName
cash = 0
AI = True

units = {
    hobbits: 9,
    hobbit_archers: 3,
    tooks: 3,
}

heroes = (
    bombadil,
    cotton,
    frodo,
    sam,
)

allies = [
    BeorningsName,
    DunedainName,
    DwarvesName,
    EntsName,
    GondorName,
    HighElvesName,
    RohanName,
    SilvanElvesName,
    SindarElvesName,
]