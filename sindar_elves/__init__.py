from .army import *
from lists_dictionaries.faction_names import SindarElvesName, DunedainName, EntsName, HalflingsName, HighElvesName, SilvanElvesName

name = SindarElvesName
cash = 0
subname = 'Avari'
AI = True

units = {
    lorien_infantry: 4,
    lorien_archers: 5,
    lorien_spearmen: 4,
    sindar_lancers: 3,
}

heroes = (
    galadriel,
    celeborn
)

allies = [
    DunedainName,
    EntsName,
    HalflingsName,
    HighElvesName,
    SilvanElvesName,
]