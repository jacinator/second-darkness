from lists_dictionaries.territory_list import TerritoryList
from functions.units import PrintUnits
from lists_dictionaries.heros_units_dictionary import UnitDictionary

class TerritoryInterface(object):
    def __init__(self, Territory, CurrentFaction):
        self.Territory = Territory
        self.CurrentFaction = CurrentFaction
        self.command = 'initial command'
        self.commands = {
            'exit': 'exit',
            'done': 'done',
            'cancel': 'done',
            
            'recruit': 'recruit',
            'move': 'move',
            'parade': 'parade',
            'build': 'build',
            'attack': 'attack',
            'disband': 'disband',
            'destroy': 'destroy',
            'sack': 'sack',
            'map': 'map',
            'other': 'other',
            'money': 'cash',
            'cash': 'cash',
        }
    
    def Recruit(self):
        print('Which unit would you like to recruit?')
        PrintUnits(self.CurrentFaction, self.Territory)
        print("%s's resources: $%d" % (self.CurrentFaction.name, self.CurrentFaction.cash))
        
        Unit = input('%s > Recruitment > ' % self.Territory.name).lower()
        try:
            Unit = UnitDictionary[Unit]
        except KeyError:
            if Unit != 'cancel':
                print(InvalidUnit % Unit.capitalize())
            return
        print('How many %s would you like to recruit?' % Unit.name)
        try:
            UnitNumber = int(input('%s > Recruitment > %s > ' % (self.Territory.name, Unit.name)))
        except ValueError:
            if Unit != 'cancel':
                UnitNumber = 1
            else:
                return
        self.Territory.hire(Unit, UnitNumber)
    
    def Move(self):
        if self.Territory.occupants == self.CurrentFaction or self.CurrentFaction.name in self.Territory.occupants.allies:
            print("Where would you like to move %s's army?" % self.Territory.name)
            for land in TerritoryList:
                if land.name in self.Territory.neighbours:
                    if land.occupants == self.CurrentFaction:
                        if land.recruitment == False or land.city == land.name:
                            print(" - %s" % land.name)
                        else:
                            print(" - %s, %s" % (land.city, land.name))
                    elif land.occupants.name in self.CurrentFaction.allies:
                        if land.recruitment == False or land.city == land.name:
                            print(" - %s, allied" % land.name)
                        else:
                            print(" - %s, %s, allied" % (land.city, land.name))
            Destination = input('%s > Movement > ' % self.Territory.name).lower()
            try:
                for Territory in TerritoryList:
                    if Destination in Territory.InterfaceName():
                        self.Territory.move(Territory, self.CurrentFaction)
            except KeyError:
                print(InvalidTerritory % Destination)
    
    def Parade(self):
        self.Territory.parade()
    
    def Build(self):
        self.Territory.build()
    
    def Attack(self):
        if self.Territory.occupants == self.CurrentFaction or self.CurrentFaction.name in self.Territory.occupants.allies:
            print("Where would you like to attack?")
            for land in TerritoryList:
                if land.name in self.Territory.neighbours:
                    if land.occupants != self.CurrentFaction and land.occupants not in self.CurrentFaction.allies:
                        if land.recruitment == False:
                            print(" - %s" % land.name)
                        else:
                            print(" - %s, %s" % (land.city, land.name))
            Destination = input('%s > Attack > ' % self.Territory.name).lower()
            try:
                for territory in TerritoryList:
                    if Destination in territory.InterfaceName():
                        self.Territory.attack(territory, self.CurrentFaction)
            except KeyError:
                print(InvalidTerritory % Destination)
    
    def Disband(self):
        self.Territory.disband()
    
    def Destroy(self):
        self.Territory.destroy()
    
    def Sack(self):
        self.Territory.sack()
    
    def Map(self):
        self.Territory.around(TerritoryList)
    
    def Other(self):
        #print(' - Rename')
        print(' - Map')
        if self.Territory.recruitment == True:
            print(' - Sack')
            print(' - Destroy')
        if self.Territory.army != []:
            print(' - Disband')
    
    def Money(self):
        print("$%d" % self.CurrentFaction.cash)
    
    def Run(self):
        if self.Territory.recruitment == True:
            print("You have selected %s, in %s, as your base of operations." % (self.Territory.city, self.Territory.name))
        else:
            print("You have selected %s as your current base of operations." % self.Territory.name)
        
        while self.command != 'done':
            print()
            if self.command != 'other':
                print("Options:")
            if self.Territory.army != []:
                print(" - Parade")
                print(" - Attack")
                print(" - Move")
            if self.Territory.recruitment == True:
                print(" - Recruit")
            print(" - Other")
            if self.command != 'other':
                Command = input('%s > ' % self.Territory.name).lower()
            else:
                Command = input('%s > Other > ' % self.Territory.name).lower()
            try:
                self.command = self.commands[Command]
                if self.command == 'done':
                    pass
                elif self.command == 'exit':
                    exit()
                elif self.command == 'recruit':
                    self.Recruit()
                elif self.command == 'move':
                    self.Move()
                elif self.command == 'parade':
                    self.Parade()
                elif self.command == 'build':
                    self.Build()
                elif self.command == 'attack':
                    self.Attack()
                elif self.command == 'disband':
                    self.Disband()
                elif self.command == 'destroy':
                    self.Destroy()
                elif self.command == 'sack':
                    self.Sack()
                elif self.command == 'map':
                    self.Map()
                elif self.command == 'other':
                    self.Other()
                elif self.command == 'cash':
                    self.Money()
            except KeyError:
                print("Invalid command.")
    
