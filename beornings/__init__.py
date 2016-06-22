from .army import *
from lists_dictionaries.faction_names import BeorningsName, DwarvesName, HalflingsName, SilvanElvesName

name = BeorningsName
cash = 1000
AI = True

units = (
    beorning_archers,
    beorning_infantry,
    skin_changers,
)

units = {
    beorning_archers: 2,
    beorning_infantry: 2,
    skin_changers: 5,
}

heroes = (beorn)

allies = [
    DwarvesName,
    HalflingsName,
    SilvanElvesName,
]
