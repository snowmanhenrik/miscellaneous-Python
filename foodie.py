
def chooseHouse(foodDict:int):
    peoplelist = list(foodDict)
    familylist = []
    venue = ""
    for people in peoplelist:
        poundsofgravy = 0
        poundsofturkey = 0
        if "gravy" in foodDict[people]:
            poundsofgravy = foodDict[people]["gravy"]
        else:
            poundsofgravy = 0
        if "turkey" in foodDict[people]:
            poundsofturkey = foodDict[people]["turkey"]
        else:
            poundsofturkey = 0
        if poundsofgravy + poundsofturkey >= 11:
            familylist.append(people)
    familylist.sort()

    if len(familylist) == 0:
        venue = "No one has turkey and gravy?!?"
    elif len(familylist) == 1:
        venue = "Thanksgiving will be at {}!".format(familylist[0])
    elif len(familylist) == 2:
        venue = "Thanksgiving will be at {} or {}!".format(familylist[0],familylist[1])
    else:
        venue = "Thanksgiving will be at "
        for i in range(len(familylist)):
            if i == 0:
                venue += "{}".format(familylist[i])
            elif i > 0 and i < (len(familylist)-1):
                venue += ", {}".format(familylist[i])
            elif i == (len(familylist)-1):
                venue += ", or {}!".format(familylist[i])
    return venue


def sortFood(menu:dict,order:dict):
    
    revenue = 0

    for food, quantity in order.items():
        parts = food.split(" - ")
        main_food = parts[0]

        if main_food in menu:
            subrevenue = menu[main_food]['price']
            
            if len(parts) > 1:
                addonlist = parts[1].split(", ")
                for addon in addonlist:
                    if addon in menu[main_food]:
                        subrevenue += menu[main_food][addon]

            revenue += subrevenue * quantity

    return revenue

