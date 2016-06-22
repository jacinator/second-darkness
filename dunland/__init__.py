from .army import *
from lists_dictionaries.faction_names import DunlandName, GundabadName, IsengardName

name = DunlandName
cash = 0
subname = 'Pukel-men'
AI = True

units = {
    dunlendings: 11,
    dunland_archers: 3,
}

allies = [
    GundabadName,
    IsengardName,
]