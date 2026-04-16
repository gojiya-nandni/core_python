age = int(input("Enter Yuor age : "))
# if age>=0 and age<=18:
if 0<= age <= 18:
    print("Valid age")
else:
    print("Invalid age")

marks = int(input("Enter your marks : "))
match marks:
    case 1:
        if 80 <= marks <= 100:
            print("Grade A")
    case 2:
        if 50 <= marks <= 79:
            print("Grade B")
    case 3:
        if 33<= marks <= 49:
            print("Grade C")
    case 4:
        if 0<= marks <=32:
            print("Failed")
    case _:
        print("Invalid marks")