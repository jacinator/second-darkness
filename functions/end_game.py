def DefeatAssess(faction, checklist, heroes = [], territories = []):
    for territory in checklist:
        for hero in heroes:
            if hero in territory.army:
                return False
    for territory in territories:
        if territory in checklist and territory.occupants == faction:
            return False
    return True

def CollectResources(faction, checklist, PRINT = True):
    total = 0
    for land in checklist:
        if land.occupants == faction:
            faction.cash += land.value * 10
            total += land.value * 10
    if PRINT == True:
        print("%s has collected %d resources." % (faction.name, total))