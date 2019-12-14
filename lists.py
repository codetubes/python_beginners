names = ["John","SMITH","ANDREW","Julie","Jacob"]
#print(names)

ages = [18,28,38,50,65]
#print(ages)

mixedLists = [15,28,"Andre",True]
#print(mixedLists)
#print(names[2])
#print(names[-1])

names[1] = "Arman"
#print(names)

names.append("Ben")
#print(names)

lastElement = names.pop()
#print(lastElement)

mixedLists2 = [
    ["James","Kim","Simon"],
    [15,18,39,55,78,95,-16,78]

]

#print(mixedLists2[1])
#print(mixedLists2[1][2])
totalLists = mixedLists2[0]+ mixedLists2[1]
#print(totalLists)
doubledLists = mixedLists2[0]*3
#print(doubledLists)
#print(mixedLists2[1][2:])
print(mixedLists2[1][:-2])