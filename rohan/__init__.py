from .army import *
from .heroes import *
from lists_dictionaries.faction_names import RohanName, DunedainName, GondorName, HalflingsName

name = RohanName
cash = 0
AI = True

units = {
    rohirrim: 15,
    royal_guard: 4,
    rohirric_archers: 0,
    riders: 19,
}

heroes = (
    theoden,
    eomer,
    eowyn,
    merry,
)

allies = [
    DunedainName,
    GondorName,
    HalflingsName,
]
