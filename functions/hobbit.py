from lists_dictionaries.territory_list import TerritoryList
from lists_dictionaries.faction_loop import FactionPrint, FactionLoop

import mordor
import easterlings
import dwarves
import silvan_elves
import beornings
import gundabad
import high_elves
import dunland
import halflings
import eagles

HobbitFactions = [
    mordor,
    easterlings,
    dwarves,
    silvan_elves,
    beornings,
    gundabad,
    high_elves,
    dunland,
    halflings,
    eagles,
]

def SetupHobbit():
    for Faction in FactionLoop:
        if Faction not in HobbitFactions:
            FactionPrint[Faction] = False