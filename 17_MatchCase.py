x = int(input("Enter first number:"))

match x:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case _:
        print("Default")