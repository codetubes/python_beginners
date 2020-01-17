"""
myFile = open("users.txt","r")
print(myFile.readline())
print(myFile.readline())

myFile.close()
"""
'''
with open("users.txt","r") as f:
    for line in f.readlines()[1:]:
        print(line[:-1].split(",")[2])
''' 
'''
with open("new_file.txt","a") as f:
    f.write("New File Info - with a")
'''

with open("users.txt" , "r") as f:
    for line in f.readlines()[1:]:
        info = line[:-1].split(",")
        if info[3] == "male":
            with open("males.txt","a") as mFile:
                mFile.write(line)
        elif info[3] == "female":
            with open("females.txt","a") as fFile:
                fFile.write(line)
        else:
            print("Unknown")
