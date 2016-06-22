from functions.end_game import DefeatAssess, CollectResources
from functions.strings_digits import capfirst, pluralize
from functions.iterables import first_of
from functions.ai import RunAI
from functions.units import print_units

from lists_dictionaries.territory_list import TerritoryList
from lists_dictionaries.heros_units_dictionary import HeroDictionary, UnitDictionary
from lists_dictionaries.territory_dictionary import TerritoryDictionary
from lists_dictionaries.command_dictionary import CommandDictionary
from lists_dictionaries.faction_loop import FactionLoop, EvilFactions, GoodFactions, AssessmentDictionary

from errors.command_errors import InvalidCommand, InvalidValue
from errors.territory_errors import RecruitmentError, AssaultError, BuildingError, DestroyError, DisbandError, InvalidTerritory, MovementError, RenameError, SackError, FunnyError, MapError

from templates.abilities import vision

game_done = False

for faction in FactionLoop:
    CollectResources(faction, PRINT = False, checklist = TerritoryList)

while game_done == False:
    for assessment in AssessmentDictionary:
        if AssessmentDictionary[assessment] == True:
            for faction in FactionLoop:
                if faction.name == assessment:
                    FactionLoop.remove(faction)
                    print("%s has surrendered." % faction.name)
    
    bad_count = 0
    good_count = 0
    for faction in FactionLoop:
        if faction in GoodFactions:
            good_count += 1
        else:
            bad_count += 1
    if good_count == 0:
        game_done = True
        print("Evil wins")
    if bad_count == 0:
        game_done = True
        print("Good wins")
    
    for faction in FactionLoop:
        print("%s's turn." % faction.name)
        if faction.AI == True:
            RunAI(faction, TerritoryList)
            print()
        else:
            loop_counter = 0
            while loop_counter < 4:
                print("%s's territories:" % faction.name)
                print("Please choose one.")
                for territory in TerritoryList:
                    if territory.occupants == faction:
                        print(" - %s" % territory.name)
                print('Allied territories with units.')
                for territory in TerritoryList:
                    try:
                        if first_of(territory.allies.values()).faction == faction:
                            print(" - %s" % territory.name)
                    except AttributeError:
                        pass
                base = input(' > ').lower()
                try:
                    base = TerritoryDictionary[base]
                    if base.recruitment == True:
                        print("You have selected %s, in %s, as your base of operations." % (base.city, base.name))
                    else:
                        print("You have selected %s as your current base of operations." % base.name)
                    loop_counter += 1
                    print("Options:")
                    if base.occupants == faction:
                        if base.recruitment == True:
                            print(" - Recruitment")
                        if base.army != {}:
                            print(" - Movement")
                            print(" - Parade")
                            attackable = False
                            for land in base.neighbours:
                                for country in TerritoryList:
                                    if country.name == land and country.occupants != faction:
                                        attackable = True
                            if attackable == True:
                                print(" - Attack")
                        if base.level == None or base.level < 5:
                            print(" - Building")
                        print(' - Other')
                    else:
                        if base.allies != {}:
                            print(" - Movement")
                    command = input(' > ').lower()
                    try:
                        command = CommandDictionary[command]
                        if command == 'recruit':
                            if base.occupants == faction:
                                print('Which unit would you like to recruit?')
                                print_units(faction, base)
                                print("%s's resources: $%d" % (faction.name, faction.cash))
                                unit_type = input(' > ').lower()
                                for unit in UnitDictionary:
                                    if unit_type == unit:
                                        unit_type = UnitDictionary[unit]
                                try:
                                    print('How many %s would you like to recruit?' % unit_type.name)
                                    try:
                                        unit_number = int(input(' > '))
                                    except ValueError:
                                        unit_number = 1
                                    try:
                                        base.hire(unit_type, unit_number)
                                    except ValueError:
                                        print(InvalidValue % unit_number)
                                        loop_counter -= 1
                                except AttributeError:
                                    print("%s is not a valid unit." % unit_type)
                                    loop_counter -= 1
                            else:
                                print(RecruitmentError % base.name)
                                loop_counter -= 1
                        elif command == 'build':
                            if base.occupants == faction:
                                loop_counter += 2
                                base.build()
                            else:
                                print(BuildingError % base.name)
                                loop_counter -= 1
                        elif command == 'parade':
                            base.parade()
                            loop_counter -= 1
                        elif command == 'allies':
                            base.show_allies()
                            loop_counter -= 1
                        elif command == 'move':
                            if base.occupants == faction:
                                print("Where would you like to move %s's army?" % base.name)
                                for land in base.neighbours:
                                    for country in TerritoryList:
                                        try:
                                            if country.name == land and country.occupants == faction:
                                                print(" - %s" % country.name)
                                            elif country.name == land and country.occupants.name in faction.allies:
                                                print(" - %s, allied" % country.name)
                                        except:
                                            pass
                                destination = input(' > ').lower()
                                try:
                                    base.move(TerritoryDictionary[destination])
                                except KeyError:
                                    print(InvalidTerritory % destination)
                                    loop_counter -= 1
                            elif base.occupants.name in faction.allies:
                                print("Where would you like to move your army in %s?" % base.name)
                                for land in base.neighbours:
                                    for country in TerritoryList:
                                        if country.name == land and country.occupants == faction:
                                            print(" - %s" % country.name)
                                        elif country.name == land and country.occupants.name in faction.allies:
                                            print(" - %s, allied" % country.name)
                                        else:
                                            pass
                                destination = input(' > ').lower()
                                try:
                                    base.march_allies(TerritoryDictionary[destination])
                                except KeyError:
                                    print(InvalidTerritory % destination)
                                    loop_counter -= 1
                            else:
                                print(MovementError % base.name)
                                loop_counter -= 1
                        elif command == 'attack':
                            if base.occupants == faction:
                                loop_counter += 1
                                print("Where would you like to attack?")
                                for land in base.neighbours:
                                    for country in TerritoryList:
                                        if country.name == land and country.occupants != faction:
                                            print(" - %s" % country.name)
                                target = input(' > ').lower()
                                try:
                                    base.attack(TerritoryDictionary[target])
                                except KeyError:
                                    print(InvalidTerritory % capfirst(target))
                                    loop_counter -= 1
                            else:
                                print(AssaultError % base.name)
                                loop_counter -= 1
                        elif command == 'disband':
                            if base.occupants == faction:
                                loop_counter -= 1
                                base.disband()
                            else:
                                print(DisbandError % base.name)
                                loop_counter -= 1
                        elif command == 'destroy':
                            if base.occupants == faction:
                                loop_counter += 1
                                base.destroy()
                            else:
                                print(DestroyError % base.city)
                                loop_counter -= 1
                        elif command == 'sack':
                            if base.occupants == faction:
                                loop_counter += 2
                                base.sack()
                            else:
                                print(SackError % base.city)
                                loop_counter -= 1
                        elif command == 'rename':
                            if base.occupants == faction:
                                loop_counter -= 1
                                print("What would you like to rename %s?" % base.name)
                                new_name = input(' > ')
                                base.name = new_name
                                TerritoryDictionary[new_name.lower()] = base
                            else:
                                print(RenameError % base.name)
                                loop_counter -= 1
                        elif command == 'other':
                            loop_counter -= 1
                            print(' - Disband')
                            print(' - Destroy')
                            print(' - Sack')
                            print(' - Rename')
                        elif command == 'map':
                            loop_counter -= 1
                            if base.occupants == faction:
                                seen = [base.name]
                                for place in base.neighbours:
                                    for land in TerritoryList:
                                        if land.name == place:
                                            land.report()
                                            seen.append(base.name)
                                            try:
                                                for hero in base.army.values():
                                                    if hero.ability == vision:
                                                        for place in land.neighbours:
                                                            for nieghbour in TerritoryList:
                                                                if place == nieghbour.name:
                                                                    if place in seen:
                                                                        pass
                                                                    else:
                                                                        nieghbour.report()
                                                                        seen.append(place)
                                            except KeyError:
                                                pass
                            else:
                                print(MapError % base.name)
                    except KeyError:
                        print(InvalidCommand % command)
                except KeyError:
                    try:
                        hero = HeroDictionary[base]
                        print('%s selected.' % hero.name)
                        print("Options:")
                        print(' - Ability: %s' % hero.ability.name)
                        action = input(' > ')
                        try:
                            action = CommandDictionary[action]
                            if action == 'activate':
                                hero.toggle_ability()
                        except:
                            print(FunnyError)
                    except KeyError:
                        try:
                            if CommandDictionary[base] == 'done':
                                loop_counter = 4
                            elif CommandDictionary[base] == 'exit':
                                exit()
                            elif CommandDictionary[base] == 'cash':
                                print(faction.cash)
                        except KeyError:
                            print(InvalidCommand % capfirst(base))
                            loop_counter -= 1
                print()
            else:
                CollectResources(faction, TerritoryList)
                for territory in TerritoryList:
                    for unit in list(territory.army.values()):
                        unit.ability_active = False
                print()
else:
    exit()
