from middle_earth.map_brownlands import *
from middle_earth.map_eriador import *
from middle_earth.map_gondor_rohan import *
from middle_earth.map_misty_mountains import *
from middle_earth.map_mordor import *
from middle_earth.map_wilderland import *

import monsters
from monsters.army import smaug

from functions.end_game import DefeatAssess

from .territory_list import TerritoryList

FactionLoop = [
    mordor, 
    corsairs,
    gondor,
    harad,
    easterlings,
    dwarves,
    silvan_elves,
    beornings,
    gundabad,
    sindar_elves,    
    isengard,
    ents,
    rohan,
    high_elves,
    dunland,
    halflings,
    dunedain,
    eagles,
]

FactionPrint = {
    mordor: True, 
    corsairs: True,
    gondor: True,
    harad: True,
    easterlings: True,
    dwarves: True,
    silvan_elves: True,
    beornings: True,
    gundabad: True,
    sindar_elves: True,    
    isengard: True,
    ents: True,
    rohan: True,
    high_elves: True,
    dunland: True,
    halflings: True,
    dunedain: True,
    eagles: True,
}

EvilFactions = (
    mordor, 
    corsairs,
    harad,
    easterlings,
    gundabad,
    isengard,
    dunland,
    monsters
)

GoodFactions = (
    gondor,
    eagles,
    dwarves,
    silvan_elves,
    beornings,
    sindar_elves,    
    ents,
    rohan,
    high_elves,
    halflings,
    dunedain,
)

AssessmentDictionary = {
    monsters.name: DefeatAssess(
        faction = monsters,
        heroes = [smaug],
        territories = [],
        checklist = TerritoryList,
    ),
    eagles.name: DefeatAssess(
        faction = eagles,
        heroes = [thorondor],
        territories = [eyrie],
        checklist = TerritoryList,
    ),
    mordor.name: DefeatAssess(
        faction = mordor,
        heroes = [angmar],
        territories = [dol_guldur],
        checklist = TerritoryList,
    ),
    corsairs.name: DefeatAssess(
        faction = corsairs,
        territories = [umbar],
        checklist = TerritoryList,
    ),
    gondor.name: DefeatAssess(
        faction = gondor,
        territories = [pelennor, morgul_vale],
        heroes = [faramir, boromir, aragorn],
        checklist = TerritoryList,
    ),
    harad.name: DefeatAssess(
        faction = harad,
        territories = [haradwaith],
        checklist = TerritoryList,
    ),
    easterlings.name: DefeatAssess(
        faction = easterlings,
        territories = [khand, rhun],
        heroes = [gothmog],
        checklist = TerritoryList,
    ),
    dwarves.name: DefeatAssess(
        faction = dwarves,
        heroes = [thorin, dain],
        territories = [moria, erebor, gundabad, carn_dum],
        checklist = TerritoryList,
    ),
    silvan_elves.name: DefeatAssess(
        faction = silvan_elves,
        heroes = [thranduil, legolas],
        territories = [woodland_realm],
        checklist = TerritoryList,
    ),
    beornings.name: DefeatAssess(
        faction = beornings,
        heroes = [beorn],
        territories = [carrock],
        checklist = TerritoryList,
    ),
    gundabad.name: DefeatAssess(
        faction = gundabad,
        heroes = [bolg, azog],
        territories = [moria, erebor, gundabad, carn_dum],
        checklist = TerritoryList,
    ),
    sindar_elves.name: DefeatAssess(
        faction = sindar_elves,
        heroes = [galadriel, celeborn],
        territories = [lorien],
        checklist = TerritoryList,
    ),
    isengard.name: DefeatAssess(
        faction = isengard,
        heroes = [saruman],
        territories = [nan_curunir, pelennor],
        checklist = TerritoryList,
    ),
    ents.name: DefeatAssess(
        faction = ents,
        heroes = [treebeard],
        territories = [fangorn],
        checklist = TerritoryList,
    ),
    rohan.name: DefeatAssess(
        faction = rohan,
        heroes = [theoden, eomer, eowyn, aragorn, faramir],
        territories = [westfold],
        checklist = TerritoryList,
    ),
    high_elves.name: DefeatAssess(
        faction = high_elves,
        heroes = [elrond],
        territories = [rivendell, mithlond, nan_curunir],
        checklist = TerritoryList,
    ),
    dunland.name: DefeatAssess(
        faction = dunland,
        territories = [enedwaith],
        checklist = TerritoryList,
    ),
    halflings.name: DefeatAssess(
        faction = halflings,
        heroes = [frodo, sam, cotton, aragorn],
        territories = [shire],
        checklist = TerritoryList,
    ),
    dunedain.name: DefeatAssess(
        faction = dunedain,
        heroes = [aragorn],
        territories = [north_downs],
        checklist = TerritoryList,
    ),
}