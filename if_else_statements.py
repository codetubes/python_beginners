print("===== Menu =====")
print("1. Home")
print("2. Settings")
print("3. Profile")
print("4. Exit")

print("Enter Menu ID: ")
command = input()
#command = "7"
login = True

if command == "1":
    print("Open Home Page")
elif command == "2":
    print("Open Settings Page")
elif (command == "3" or login == True) and 5>6:
    print("Open Profile Page")
else:
    print("Exit Application")