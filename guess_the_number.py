from random import randint
def generate_number():
    randomNumber = randint(0,10)
    return randomNumber



def main():
    theNumber = generate_number()
    i = 1
    while True:
        print("Guess The Number")
        number = input()

        try:
            number = int(number)
        except Exception as e:
            print("Wrong number")
            continue
        
        if number == theNumber:
            print("Congradulations...")
            print("The correct number is {} You've tried {} times".format(str(number), str(i)))
            break
        elif number > theNumber:
            print("Go Lower")
        elif number < theNumber:
            print("Go Higher")

        print("==================")
        i +=1

main()