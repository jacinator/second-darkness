from lists_dictionaries.territory_list import TerritoryList

from .territory import TerritoryInterface
from .alliance import AllianceInterface

from functions.end_game import CollectResources

from random import choice

class FactionInterface(object):
    def __init__(self, faction):
        self.Faction = faction
        self.Commands = {
            'done': 'done',
            
            'exit': 'exit',
            'exit()': 'exit',
            
            'allies': 'allies',
            'alliances': 'allies',
            
            'cash': 'cash',
            'money': 'cash',
            'resources': 'cash',
        }
        self.Territories = []
        self.LoopCounter = 0
        self.AlliedTerritories = []
    
    def AssessTerritories(self):
        self.Territories = []
        for Territory in TerritoryList:
            if Territory.occupants == self.Faction:
                self.Territories.append(Territory)
    
    def AssessAlliedTerritories(self):
        self.AlliedTerritories = []
        for Territory in TerritoryList:
            try:
                Unit = choice(Territory.allies)
                if Unit.faction == self.Faction:
                    self.AlliedTerritories.append(Territory)
            except IndexError:
                pass
    
    def PrintTerritories(self):
        print("%s's territories:" % self.Faction.name)
        print("Please choose one.")
        for territory in self.Territories:
            if territory.recruitment != True or territory.name == territory.city:
                print(" - %s" % territory.name)
            else:
                print(" - %s, %s" % (territory.city, territory.name))
        if self.AlliedTerritories != []:
            for territory in self.AlliedTerritories:
                if territory.recruitment != True:
                    print(" - %s, Allied" % territory.name)
                else:
                    print(" - %s, %s, Allied" % (territory.city, territory.name))
    
    def Run(self):
        self.AssessTerritories()
        self.AssessAlliedTerritories()
        CollectResources(self.Faction, self.Territories, PRINT = False)
        
        print("%s's turn." % self.Faction.name)
        while self.LoopCounter < 4:
            self.AssessTerritories()
            self.AssessAlliedTerritories()
            self.PrintTerritories()
            Command = input('%s > ' % self.Faction.name).lower()
            try:
                Command = self.Commands[Command]
                if Command == 'exit':
                    exit()
                elif Command == 'done':
                    self.LoopCounter = 5
                elif Command == 'allies':
                    Allies = AllianceInterface(self.Faction)
                    Allies.Run()
                elif Command == 'cash':
                    print("$%d" % self.Faction.cash)
            except KeyError:
                for Territory in self.Territories + self.AlliedTerritories:
                    if Command in Territory.InterfaceName() or Command == Territory.InterfaceName():
                        self.LoopCounter += 1
                        Base = TerritoryInterface(Territory, self.Faction)
                        Base.Run()
            print()
