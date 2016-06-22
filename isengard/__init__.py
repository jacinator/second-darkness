from .army import *
from lists_dictionaries.faction_names import IsengardName, DunlandName, GundabadName, MordorName

name = IsengardName
cash = 0
AI = True

units = {
    orcs: 7,
    uruk_hai: 20,
    warg_riders: 8,
    uruk_archers: 5,
}

heroes = (
    saruman,
    lurtz,
)

allies = [
    DunlandName,
    GundabadName,
    MordorName,
]
