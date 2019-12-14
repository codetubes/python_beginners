name = "Arman"
try:
    print(name)
except SyntaxError as e:
    print("Variable not found")
except ValueError as ex:
    print(ex)
else:
    print("Run else block")
finally:
    print("Some Errors Found")



print("continue...")