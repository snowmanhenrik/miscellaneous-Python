def organizeTimes(unorganizedTimeList:list):
    semiorganizedTimeList = []
    organizedTimeList = []
    for time,name in unorganizedTimeList:
        time = list(time)
        time.remove(max(time))
        time.sort()
        semiorganizedTimeList = (name,time)
        organizedTimeList.append(semiorganizedTimeList)
        organizedTimeList.sort()
