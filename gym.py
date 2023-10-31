
import calendar

def bestMachine(machines:list,rating:list):
    highestRated = []
    for i in range(len(rating)):
        if rating[i] == max(rating):
            tuplelist = (machines[i],rating[i])
            highestRated.append(tuplelist)
    highestRated.sort()
    return highestRated
            
def whenGoToGym(freeTime:list):
    disclist = []
    for name,time in freeTime:
        discriminant = 0
        for i in range(len(time)):
            if calendar.weekday(2023,time[i][0],time[i][1]) == 0:
                discriminant += 1
            elif calendar.weekday(2023,time[i][0],time[i][1]) == 3:
                discriminant += 1
            elif calendar.weekday(2023,time[i][0],time[i][1]) == 4:
                discriminant +=1
            else:
                discriminant +=0
        disclist.append(discriminant)
    if 0 not in disclist:
        everyoneCanGo = True
    else:
        everyoneCanGo = False
    return everyoneCanGo
    
        




 


    
        
        


#########################################
