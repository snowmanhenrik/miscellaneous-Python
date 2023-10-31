def bulkOrder(foodCatalog:list):
    foodlist = []
    foodsAndPrice = []
    foodprice = 0
    for foodName,price,protein in foodCatalog:
        if protein >= 20 and price < 8:
            foodlist.append(foodName)
            foodprice += price

    foodlist.sort()
    foodsAndPrice.append(foodlist)
    foodsAndPrice.append(foodprice)
    return foodsAndPrice
