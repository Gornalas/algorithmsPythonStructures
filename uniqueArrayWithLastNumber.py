oldArray = [1, 5, 5, 1, 6, 1]
newArray = []

def uniqueArray(oldArray):
    for index in oldArray:
        if index in newArray:
            newArray.remove(index)
        newArray.append(index)
    print(newArray)

uniqueArray(oldArray)
