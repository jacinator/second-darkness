class faction(object):
    def __init__(self, name, units, heroes, allies, territories = []):
        self.name = name
        self.territories = territories
        self.units = units
        self.heroes = heroes
        self.cash = 1000
        self.allies = allies
    
    def print_allies(self):
        for ally in self.allies:
            print(ally.name)