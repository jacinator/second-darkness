from .army import *
from lists_dictionaries.faction_names import CorsairsName, HaradName, EasterlingsName, MordorName

name = CorsairsName
cash = 1000
AI = True

units = {
    corsair_archers: 4,
    pirates: 7,
}

allies = [
    HaradName,
    EasterlingsName,
    MordorName,
]
