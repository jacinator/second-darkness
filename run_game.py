from middle_earth.map_eriador import *

from lists_dictionaries.territory_list import TerritoryList
from lists_dictionaries.faction_loop import FactionLoop, AssessmentDictionary

from interface.faction import FactionInterface
from functions.ai import RunAI

gamewon = False
while gamewon == False:
    for Faction in FactionLoop:
        if AssessmentDictionary[Faction.name] != True:
            if Faction.AI == False:
                print()
                FactionInterface(Faction).Run()
            else:
                print("%s's turn" % Faction.name)
                RunAI(Faction, TerritoryList)
        else:
            print("%s has been defeated." % Faction.name)
            FactionLoop.remove(Faction)
    
