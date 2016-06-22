from .army import *
from lists_dictionaries.faction_names import EasterlingsName, CorsairsName, HaradName, MordorName

name = EasterlingsName
cash = 0
AI = True

units = {
    easterling_archers: 3,
    easterling_infantry: 7,
    lancers: 0,
    variags: 8,
}

heroes = (gothmog)

allies = [
    CorsairsName,
    HaradName,
    MordorName,
]
