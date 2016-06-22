from middle_earth.map_brownlands import *
from middle_earth.map_eriador import *
from middle_earth.map_gondor_rohan import *
from middle_earth.map_misty_mountains import *
from middle_earth.map_mordor import *
from middle_earth.map_wilderland import *

from functions.ai import RunAI
from functions.iterables import FirstOf
from functions.strings_digits import capfirst, EvenDivide, SearchCapitalization
from functions.interface import TerritoryInterface, AllianceInterface, FactionInterface
from functions.end_game import CollectResources
from functions.units import GetType
from functions.hobbit import SetupHobbit

from errors.territory_errors import InvalidTerritory

from templates.units import hero

from lists_dictionaries.territory_list import TerritoryList
#from lists_dictionaries.territory_dictionary import TerritoryDictionary
from lists_dictionaries.faction_loop import EvilFactions, GoodFactions, FactionLoop, AssessmentDictionary, FactionPrint
from lists_dictionaries.command_dictionary import CommandDictionary

GameDone = False

while GameDone == False:
    GoodFactionCount = 0
    EvilFactionCount = 0
    
    for Faction in FactionLoop:
        if Faction in GoodFactions:
            GoodFactionCount += 1
        elif Faction in EvilFactions:
            EvilFactionCount += 1
    
    if EvilFactionCount <= 0 or GoodFactionCount <= 0:
        GameDone = True
        print("Surviving factions:")
        for Faction in FactionLoop:
            print(" - %s" % Faction.name)
    
    for Faction in FactionLoop:
        if Faction.AI == False:
            CollectResources(Faction, TerritoryList)
            Faction = FactionInterface(Faction)
            Faction.ReassessSelf()
            Faction.run()
        else:
            CollectResources(Faction, TerritoryList, PRINT = False)
            RunAI(Faction, TerritoryList)
