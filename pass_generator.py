import string
import random
def generate_password(theLength):
    """ This function generates password """
    letters = string.ascii_letters
    digits = string.digits
    totalChars = letters+digits
    finalResult = ""
    for i in range(theLength):
        finalResult+=random.choice(totalChars)
    
    return finalResult

def main():
    while True:
        print("Enter the password length")
        theLength = input()
        try:
            theLength = int(theLength)
        except Exception as e:
            print("wrong password length")
            continue
        
        thePassword = generate_password(theLength)
        print("The Password is : "+thePassword)
        
main()