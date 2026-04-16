print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
choice = int(input("Enter choice "))
num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))
match choice:
    case 1:
        print(f"Addition {num1+num2}")
    case 2:
        print(f"Substraction {num1-num2}")
    case 3:
        print(f"Multiplication {num1*num2}")
    case 4:
        print(f"Division {int(num1/num2)}")
    case _:
        print("Invalid Choice")