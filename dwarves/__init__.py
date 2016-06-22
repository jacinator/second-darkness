from .army import *
from .heroes import *
from lists_dictionaries.faction_names import DwarvesName, BeorningsName, DunedainName, GondorName, HalflingsName, HighElvesName

name = DwarvesName
cash = 0
subname = 'Khazad'
AI = True

units = {
    dragon_veterans: 6,
    dwarven_spearmen: 12,
    dwarven_archers: 7,
    dwarven_veterans: 8,
    watchmen: 4,
}

heroes = (
    bilbo,
    thorin,
    dwalin,
    balin,
    oin,
    gloin,
    fili,
    kili,
    dori,
    ori,
    nori,
    bifur,
    bofur,
    bombur,
    dain,
    gimli,
    bard,
)

allies = [
    BeorningsName,
    DunedainName,
    GondorName,
    HalflingsName,
    HighElvesName,
]
