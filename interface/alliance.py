from lists_dictionaries.faction_loop import FactionLoop, GoodFactions, EvilFactions

from random import choice

True2False2 = ('YES', 'YES', 'NO', 'NO')
True1False3 = ('YES', 'NO', 'NO', 'NO')

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
    
    def Run(self):
        for Faction in FactionLoop:
            if Faction.name not in self.faction.allies:
                print(" - %s" % Faction.name)
            else:
                print(" - %s, Ally" % Faction.name)
        
        InteractFaction = input("%s > Alliances > " % self.faction.name).lower()
        for Faction in FactionLoop:
            if Faction.name.lower() == InteractFaction:
                if Faction.name in self.faction.allies:
                    print("Are you sure you want to break your alliance with %s?" % Faction.name)
                else:
                    print("Are you sure you want to forge an alliance with %s?" % Faction.name)
                Confirmation = input('%s > Alliances > %s > ' % (self.faction.name, Faction.name)).upper()
                if Confirmation == 'YES':
                    if Faction.name in self.faction.allies:
                        self.dissolve(Faction)
                    else:
                        self.create(Faction)