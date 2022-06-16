n = list(input().split())
goods, basket = int(n[0]), int(n[1])
stuff = []
stolen = 0
for i in range(goods):
    good = list(input().split())
    goodSum, goodQuantity = int(good[0]), int(good[1])
    goodCost = goodSum / goodQuantity
    tempTuple = (goodCost, goodQuantity)
    stuff.append(tempTuple)
stuff.sort(key = lambda x: (x[0], x[1]), reverse = True)
for cost, quantity in stuff:
    if(basket >= quantity):
        basket -= quantity
    else:
        quantity = basket
        basket = 0
    stolen += quantity * cost
    if(basket == 0): break
print('%.3f' % stolen)
