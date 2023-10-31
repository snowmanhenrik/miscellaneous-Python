def showFinder(showPreferences:dict):
    peopleList = list(showPreferences)
    watchList = []
    for i in showPreferences:
        for movie in range(len(showPreferences[i])):
            watchList.append(showPreferences[i][movie])
    Intdict = dict.fromkeys(watchList)

    for Entity in Intdict:
        if not isinstance(Intdict[Entity], list):
            Intdict[Entity] = []
        for person in peopleList:
            if Entity in showPreferences.get(person):
                Intdict[Entity].append(person)
                Intdict[Entity].sort()
    watchDict = Intdict
    return watchDict
