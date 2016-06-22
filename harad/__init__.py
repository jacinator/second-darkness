from .army import *
from lists_dictionaries.faction_names import HaradName, CorsairsName, EasterlingsName, MordorName

name = 'Harad'
cash = 0
subname = 'Southrons'
AI = False

units = {
    haradrim: 24,
    southrons: 7,
    mumak: 6,
    harad_archers: 9,
    troll_men: 2,
}

allies = [
    CorsairsName,
    EasterlingsName,
    MordorName,
]
