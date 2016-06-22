def FirstOf(itemlist, item = None):
    if item == None:
        for thing in itemlist:
            return thing
    else:
        for thing in itemlist:
            if thing == item:
                return thing
