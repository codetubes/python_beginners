

def print_hello(fromWho, to):
    print("Hello from "+fromWho + " to "+to)


#print_hello("Julie", "Arman")
#print_hello("Andrew", "Smith")

def sum(numberOne=0, numberTwo=0):
    print(numberOne+numberTwo)

'''
myVar = "Some Text"
varTwo = 598
print(type(myVar))
print(type(varTwo))
print(type(str(varTwo)))
'''
'''
import os
dirpath = os.getcwd()
print("Current Directory: "+dirpath)

from datetime import datetime
print(datetime.today())
'''
#sum(9)
def doubled(x):
    x *=2
    return x

finalResult = doubled(10)
#print(finalResult)

myString = "Hello World"
def changeString():
    name = "Arman"
    print(name)
    #print(myString)
    #global myString
    #myString+=" From Arman"

changeString()
#print(name)
#print(myString)

