data = {"John":2500,"Julie":1500,"Simon":3500}
#print(data)

#print(data["Julie"])
data2 = {
    "boys":["Arman","Rick","Andrew","Smith"],
    "girls":["Julie","Laura","Nicole","Kim"]
}

#print(data2["girls"])
#print(data.get("Arman"))
data["Julie"] = 2200
#print(data)

data2["girls"].append("Anna")
#print(data2)

data.update({"Julie":3600,"Simon":3300})
#print(data)
print(data2.keys())
print(data2.values())

