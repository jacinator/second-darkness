from random import choice, randint

from functions import strings_digits, units, iterables, war

from errors.unit_errors import ExpensiveUnit

city_levels = {
    'level 1': {
        'type': 'village',
        'upgrade cost': 100,
    },
    'level 2': {
        'type': 'town',
        'upgrade cost': 200,
    },
    'level 3': {
        'type': 'city',
        'upgrade cost': 400,
    },
    'level 4': {
        'type': 'citadel',
        'upgrade cost': 800,
    },
    'level 5': {
        'type': 'tower',
        'upgrade cost': 1200,
    },
}

city_options = {
    'sack': 'sack',
    'destroy': 'destroy',
    'occupy': 'occupy',
    'stay': 'occupy',
}

class territory(object):
    def __init__(self, name, occupants, neighbours, value = 1, subname = None, army = [], recruitment = False, city_name = None, city_level = 0):
        self.name = name
        self.subname = subname
        self.occupants = occupants
        self.value = value
        self.neighbours = neighbours
        self.army = army
        self.recruitment = recruitment
        self.city = city_name
        self.level = city_level
        self.allies = []
        self.AI = self.occupants.AI
    
    def InterfaceName(self):
        self.interactivename = self.name.replace('-', ' ').replace("'", '').lower()
        if self.interactivename.startswith('the ') == True:
            self.interactivename = self.interactivename[4:]
        if self.city == None:
            self.InteractiveNames = (self.interactivename)
        else:
            self.interactivecity = self.city.replace('-', ' ').replace("'", '').lower()
            if self.interactivecity.startswith('the ') == True:
                self.interactivecity = self.interactivecity[4:]
            self.InteractiveNames = (self.interactivename, self.interactivecity)
        return self.InteractiveNames
    
    #Territory related
    
    #prints all neighbours
    def around(self, TerritoryList):
        for Territory in TerritoryList:
            if Territory.name  in self.neighbours:
                Territory.report()
    
    #Prints the territory and city information
    def report(self):
        print('--------------------------------------------------------------------------------')
        if self.recruitment == True:
            print('%s, %s' % (self.city, self.name))
        else:
            print(self.name)
        print('Land value: %d' % self.value)
        if self.occupants == None:
            print('%s is unoccupied.' % self.name)
        else:
            print('%s is occupied by %s.' % (self.name, self.occupants.name))
        if self.army == {} and self.allies == {}:
            print("%s has no army." % self.name)
        else:
            self.parade()
        print('--------------------------------------------------------------------------------')
    
    #Increases the resource value of the territory
    def develope(self):
        if self.value <= 10:
            develope_cost = 500
        else:
            develope_cost = 1500
        if self.occupants.cash >= develope_cost:
            self.value += 1
            self.occupants.cash -= develope_cost
            print("%s has been further developed" % self.name)
        else:
            print("%s does not have enough resources to further develope %s." % (self.occupants.name, self.name))
    
    #City related
    
    #If there is no city, this function build one
    #Otherwise it expands the city
    def build(self):
        if self.recruitment != False:
            if self.level < 5:
                if self.occupants.cash >= city_levels['level %d' % (self.level + 1)]['upgrade cost']:
                    self.occupants.cash -= city_levels['level %d' % (self.level)]['upgrade cost']
                    self.level += 1
                    print(" -$%d" % city_levels['level %d' % self.level]['upgrade cost'])
                    print("%s has been built up to a %s." % (self.city, city_levels['level %d' % self.level]['type']))
                else:
                    print("%s do not have enough resources to expand %s." % (strings_digits.capfirst(self.occupants.name), self.city))
            else:
                print("%s is already a tower and cannot be further developed" % strings_digits.capfirst(self.city))
        else:
            self.level = 1
            self.recruitment = True
            print("What would you like to name your city: ")
            self.city = strings_digits.capfirst(input("> "))
            self.occupants.cash -= city_levels['level 1']['upgrade cost']
            print("A village named %s has been built in %s." % (self.city, self.name))
    
    #Deletes the city
    def destroy(self):
        if self.city:
            print("%s in %s has been destroyed." % (self.city, self.name))
        self.recruitment = False
        self.city = None
        self.level = None
    
    #Nets resources from the city, but also lowers the city's level
    def sack(self):
        if self.recruitment == True:
            if 4 > self.level > 2:
                self.level -= 2
                amount = city_levels['level ' + str(self.level + 1)]['upgrade cost'] + city_levels['level ' + str(self.level + 2)]['upgrade cost']
                self.occupants.cash += amount
                print("%s's cash: +$%d." % (self.occupants.name, amount))
                city = self.city
            else:
                city = self.city
                self.occupants.cash += 300
                self.level = None
                self.city = None
                self.recruitment = False
                print("%s's cash: +$300." % self.occupants.name)
            print('%s has been sacked.' % city)
    
    #Army related
    
    #Prints all units
    def parade(self):
        print("%s's army:" % self.name)
        unit_count = {}
        for unit in self.army + self.allies:
            if unit.name in unit_count.keys():
                unit_count[unit.name]['number'] += 1
            else:
                unit_count[unit.name] = {'number': 1, 'type': units.GetType(unit)}
        for unit in unit_count.keys():
            if unit_count[unit]['type'] != 'hero':
                print("%d %s of %s." % (unit_count[unit]['number'], strings_digits.pluralize('unit', unit_count[unit]['number']), unit))
            else:
                print(unit)
    
    #Deletes all units
    def disband(self):
        self.army = {}
    
    #Creates new units
    def hire(self, unit, number = 1):
        faction_units = self.occupants.units
        recruited = 0
        for faction_unit in faction_units.keys():
            if faction_unit == unit:
                for X in range(number):
                    if unit.cost <= self.occupants.cash:
                        self.occupants.cash -= unit.cost
                        recruited += 1
                        faction_units[faction_unit] += 1
                        self.army.append(unit)
                    else:
                        if self.AI == False:
                            print(ExpensiveUnit % (unit.name, self.occupants.name))
                            if recruited > 0:
                                print("%d %s recruited." % (recruited, faction_unit.name))
                        return
        if self.AI == False:
            print("%d %s recruited." % (recruited, faction_unit.name))
    
    def move(self, destination, current_faction):
        if self.occupants == current_faction:
            if destination.occupants == self.occupants:
                destination.army += self.army
                self.army = []
            elif destination.occupants.name in self.occupants.allies:
                try:
                    TestUnit = choice(destination.allies)
                    if TestUnit.faction == self.occupants:
                        destination.allies += self.army
                        self.army = []
                    else:
                        return
                except IndexError:
                    destination.allies += self.army
                    self.army = []
        elif current_faction.name in self.occupants.allies:
            if destination.occupants == current_faction:
                destination.army += self.allies
                self.allies = []
            elif destination.occupants.name in current_faction.allies:
                try:
                    TestUnit = choice(destination.allies)
                    if TestUnit.faction == current_faction:
                        destination.allies += self.allies
                        self.allies = []
                    else:
                        return
                except IndexError:
                    destination.allies += self.allies
                    self.allies = []
    
    def attack(self, target, current_faction, AI = False):
        if current_faction.AI == True and target.AI == False:
            print("%s has attacked %s." % (current_faction.name, target.name))
        if target.occupants == self.occupants:
            if current_faction.AI == False:
                print("%s cannot attack themselves." % current_faction.name)
        elif target.occupants.name in current_faction.allies:
            if current_faction.AI == False:
                print("%s cannot attack their allies." % current_faction.name)
        else:
            if self.occupants == current_faction:
                fight = war.battle(self, target, current_faction)
            else:
                fight = war.battle(self, target, current_faction, self.allies)
            fight.fight()
            if current_faction.AI == False or target.AI == False:
                fight.stats()
            if target.occupants == current_faction:
                self.move(target, current_faction)
                if current_faction.AI == False or target.AI == False:
                    print("%s has been conquered by %s." % (target.name, self.occupants.name))
                    self.move(target, current_faction)
        if current_faction.AI == False or target.AI == False:
            print()