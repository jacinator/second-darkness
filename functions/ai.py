from random import choice, randint
from middle_earth.map_brownlands import dead_marshes
from .end_game import CollectResources
from lists_dictionaries.territory_list import TerritoryList

TrueFalse = (True, True, False)

def TerritoryArmyCheck(checklist):
    for territory in checklist:
        if territory.army == {}:
            return True
    return False

def RunAI(faction, Territorylist):
    FactionTerritories = []
    for territory in Territorylist:
        if territory.occupants == faction:
            FactionTerritories.append(territory)
    
    Loopcounter = 0
    CollectResources(faction = faction, PRINT = False, checklist = TerritoryList)
    while Loopcounter < 4:
        WillAttack = choice(TrueFalse)
        while WillAttack == True:
            Loopcounter += 2
            BaseChoiceList = []
            for Territory in FactionTerritories:
                for Potential in TerritoryList:
                    if Territory.army != {}:
                        try:
                            if Potential.name in Territory.neighbours and Potential.occupants.name not in faction.allies and Potential.occupants != faction:
                                BaseChoiceList.append(Territory)
                        except AttributeError:
                            if Potential.occupants == None and Potential.name in Territory.neighbours:
                                BaseChoiceList.append(Territory)
            try:
                AttackBase = choice(BaseChoiceList)
                AttackChoiceList = []
                for Territory in TerritoryList:
                    try:
                        if Territory.name in AttackBase.neighbours and Territory.occupants != faction and Territory.occupants.name not in faction.allies:
                            AttackChoiceList.append(Territory)
                    except AttributeError:
                        if Territory.occupants == None:
                            AttackChoiceList.append(Territory)
                try:
                    AttackTarget = choice(AttackChoiceList)
                    if AttackTarget.occupants.AI == False:
                        AttackBase.attack(AttackTarget, faction)
                    else:
                        AttackBase.attack(AttackTarget, faction, AI = True)
                except IndexError:
                    pass
            except IndexError:
                pass
            WillAttack = choice(TrueFalse)
        
        WillRecruit = choice(TrueFalse)
        while WillRecruit == True:
            Loopcounter += 1
            RecruitmentOptions = []
            for Territory in FactionTerritories:
                if Territory.recruitment == True:
                    RecruitmentOptions.append(Territory)
            try:
                Centre = choice(RecruitmentOptions)
                
                UnitChoices = []
                for unit in faction.units.keys():
                    if unit.level <= Centre.level:
                        UnitChoices.append(unit)
                NumberofUnits = randint(1, 25)
                Unit = choice(UnitChoices)
                Centre.hire(unit = Unit, number = NumberofUnits)
            except IndexError:
                pass
            WillRecruit = choice(TrueFalse)
        
        TerritoryArmyEmpty = TerritoryArmyCheck(FactionTerritories)
        if TerritoryArmyEmpty == True:
            Loopcounter += 1
            WillMove = choice(TrueFalse)
            if WillMove == True:
                BaseChoiceList = []
                for territory in FactionTerritories:
                    if territory.army != {}:
                        BaseChoiceList.append(territory)
                try:
                    MoveBase = choice(BaseChoiceList)
                    
                    DestinationChoices = []
                    for territory in FactionTerritories:
                        if territory.name in MoveBase.neighbours:
                            DestinationChoices.append(territory)
                    DestinationBase = choice(DestinationChoices)
                    
                    MoveBase.move(DestinationBase, faction)
                except IndexError:
                    pass
            TerritoryArmyEmpty = TerritoryArmyCheck(FactionTerritories)
