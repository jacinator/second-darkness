from lists_dictionaries.territory_list import TerritoryList
from lists_dictionaries.heros_units_dictionary import UnitDictionary
from lists_dictionaries.faction_loop import FactionLoop, GoodFactions, EvilFactions, AssessmentDictionary
from lists_dictionaries.command_dictionary import CommandDictionary

from errors.territory_errors import InvalidTerritory
from errors.unit_errors import InvalidUnit

from functions.strings_digits import capfirst, SearchCapitalization
from functions.units import PrintUnits
from functions.end_game import CollectResources

from random import choice

True2False2 = ('YES', 'YES', 'NO', 'NO')
True1False3 = ('YES', 'NO', 'NO', 'NO')

class TerritoryInterface(object):
    def __init__(self, Territory, CurrentFaction):
        self.faction = Territory.occupants
        self.territory = Territory
        self.CurrentFaction = CurrentFaction
    
    def Recruit(self):
        print('Which unit would you like to recruit?')
        PrintUnits(self.faction, self.territory)
        print("%s's resources: $%d" % (self.faction.name, self.faction.cash))
        
        Unit = input(' > ').lower()
        try:
            Unit = UnitDictionary[Unit]
        except KeyError:
            if Unit != 'cancel':
                print(InvalidUnit % capfirst(Unit))
            return
        print('How many %s would you like to recruit?' % Unit.name)
        try:
            UnitNumber = int(input(' > '))
        except ValueError:
            if Unit != 'cancel':
                UnitNumber = 1
            else:
                return
        self.territory.hire(Unit, UnitNumber)
    
    def Move(self):
        if self.faction == self.CurrentFaction or self.CurrentFaction.name in self.faction.allies:
            print("Where would you like to move %s's army?" % self.territory.name)
            for land in TerritoryList:
                if land.name in self.territory.neighbours:
                    if land.occupants == self.CurrentFaction:
                        print(" - %s" % land.name)
                    elif land.occupants.name in self.CurrentFaction.allies:
                        print(" - %s, allied" % land.name)
            Destination = input(' > ').lower()
            try:
                for territory in TerritoryList:
                    if Destination in territory.InterfaceName():
                        self.territory.move(territory, self.CurrentFaction)
            except KeyError:
                print(InvalidTerritory % Destination)
    
    def Parade(self):
        self.territory.parade()
    
    def Build(self):
        self.territory.build()
    
    def Attack(self):
        if self.faction == self.CurrentFaction:
            print("Where would you like to attack?")
            for land in TerritoryList:
                if land.name in self.territory.neighbours:
                    if land.occupants != self.CurrentFaction and land.occupants not in self.CurrentFaction.allies:
                        print(" - %s" % land.name)
            Destination = input(' > ').lower()
            try:
                for territory in TerritoryList:
                    if Destination in territory.InterfaceName():
                        self.territory.attack(territory, self.CurrentFaction)
            except KeyError:
                print(InvalidTerritory % Destination)
    
    def Disband(self):
        self.territory.disband()
    
    def Destroy(self):
        self.territory.destroy()
    
    def Sack(self):
        self.territory.sack()
    
    def Map(self):
        self.territory.around(TerritoryList)
    
    def Other(self):
        #print(' - Rename')
        print(' - Map')
        if self.territory.recruitment == True:
            print(' - Sack')
            print(' - Destroy')
        if self.territory.army != []:
            print(' - Disband')
    
    def Money(self):
        print("$%d" % self.faction.cash)
    
    def Exit(self):
        Verify = input("Are you sure you want to quit? ").upper()
        if Verify == 'YES':
            exit()
        else:
            pass
    
    def Run(self):
        if self.territory.recruitment == False or self.territory.city == self.territory.name:
            print("You have selected %s as your current base of operations." % self.territory.name)
        else:
            print("You have selected %s, in %s, as your base of operations." % (self.territory.city, self.territory.name))
        
        command = 'continue'
        while command != 'done':
            print("Options:")
            if self.territory.army != []:
                print(" - Parade")
                print(" - Attack")
                print(" - Move")
            if self.territory.recruitment == True:
                print(" - Recruit")
            print("Other")
            command = input(' > ').lower()
            if command == 'parade':
                self.Parade()
            elif command == 'attack':
                self.Attack()
            elif command == 'move':
                self.Move()
            elif command == 'recruit':
                self.Recruit()
            elif command == 'other':
                self.Other()
            elif command == 'map':
                self.Map()
            elif command == 'sack':
                self.Sack()
            elif command == 'destroy':
                self.Destroy()
            elif command == 'build':
                self.Build()
        else:
            return

class AllianceInterface(object):
    def __init__(self, faction):
        self.faction = faction
    
    def create(self, NewAlly):
        if NewAlly.AI == True:
            if self.faction in GoodFactions and NewAlly in GoodFactions or self.faction in EvilFactions and NewAlly in EvilFactions:
                Response = choice(True2False2)
            else:
                Response = choice(True1False3)
        else:
            Response = input("Will %s accept the proposed alliance? " % NewAlly.name).upper()
        if Response == 'YES':
            self.faction.allies.append(NewAlly.name)
            NewAlly.allies.append(self.faction.name)
            print("%s has allied with %s." %(self.faction.name, NewAlly.name))
        else:
            print("%s has refused to form an alliance with %s." % (NewAlly.name, self.faction.name))
    
    def dissolve(self, OldAlly):
        self.faction.allies.remove(OldAlly.name)
        OldAlly.allies.remove(self.faction.name)
        print("%s has broken their alliance with %s." % (self.faction.name, OldAlly.name))
    
    def run(self):
        for Faction in FactionLoop:
            if Faction.name not in self.faction.allies:
                print(" - %s" % Faction.name)
            else:
                print(" - %s, Ally" % Faction.name)
        
        InteractFaction = input(" > ").lower()
        for Faction in FactionLoop:
            if Faction.name.lower() == InteractFaction:
                if Faction.name in self.faction.allies:
                    print("Are you sure you want to break your alliance with %s?" % Faction.name)
                else:
                    print("Are you sure you want to forge an alliance with %s?" % Faction.name)
                Confirmation = input(' > ').upper()
                if Confirmation == 'YES':
                    if Faction.name in self.faction.allies:
                        self.dissolve(Faction)
                    else:
                        self.create(Faction)

class FactionInterface(object):
    def __init__(self, faction):
        self.faction = faction
        self.territories = []
        self.AlliedTerritories = []
        self.Loopcounter = 0
        self.assessment = AssessmentDictionary[self.faction.name]
        for territory in TerritoryList:
            if territory.occupants == self.faction:
                self.territories.append(territory)
    
    def ReassessSelf(self):
        self.assessment = AssessmentDictionary[self.faction.name]
    
    def AssessTerritories(self):
        self.territories = []
        for territory in TerritoryList:
            if territory.occupants == self.faction:
                self.territories.append(territory)
    
    def AssessAlliedTerritories(self):
        self.AlliedTerritories = []
        for territory in self.territories:
            try:
                unit = choice(territory.allies)
                if unit.faction == self.faction:
                    self.AlliedTerritories.append(territory)
            except IndexError:
                pass
    
    def PrintTerritories(self):
        print("%s's territories:" % self.faction.name)
        print("Please choose one.")
        for territory in self.territories:
            if territory.recruitment != True:
                print(" - %s" % territory.name)
            else:
                print(" - %s, %s" % (territory.city, territory.name))
        if self.AlliedTerritories != []:
            for territory in self.AlliedTerritories:
                if territory.recruitment != True:
                    print(" - %s, Allied" % territory.name)
                else:
                    print(" - %s, %s, Allied" % (territory.city, territory.name))
    
    def run(self):
        if self.assessment == False:
            print("%s's turn" % self.faction.name)
            command = ''
            while self.Loopcounter < 4 and command != 'done':
                self.AssessTerritories()
                self.AssessAlliedTerritories()
                self.PrintTerritories()
                
                Command = input(' > ')
                try:
                    for territory in TerritoryList:
                        if Command in territory.InterfaceName():
                            base = territory
                    Base = TerritoryInterface(base, self.faction)
                    Base.Run()
                    self.Loopcounter += 1
                except UnboundLocalError:
                    if Command[:4] != 'find' and Command[:6] != 'search':
                        try:
                            command = CommandDictionary[Command]
                            if command == 'hobbit':
                                SetupHobbit()
                            if command == 'done':
                                pass
                            if command == 'alliances':
                                Alliances = AllianceInterface(self.faction)
                                Alliances.run()
                            if command == 'cash':
                                print("%s's resources: $%d" % (self.faction.name, self.faction.cash))
                            if command == 'exit':
                                exit()
                        except KeyError:
                            print(InvalidTerritory % capfirst(Command))
                    else:
                        search = SearchCapitalization(Command)
                        for Territory in TerritoryList:
                            for Unit in Territory.army:
                                if Unit.name == search:
                                    print("%s is in %s." % (Unit.name, Territory.name))
                            if Territory.city == search or Territory.name == search:
                                print(Territory.report())
                print()
        else:
            print("%s has been eliminated." % self.faction.name)
            FactionLoop.remove(self.faction)
