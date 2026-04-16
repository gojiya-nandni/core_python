marks = int(input("Enter Your Marks : "))
if marks<=100 and marks>=70:
    print("Your grade is A")
elif marks<=69 and marks>=60:
    print("Your grade is B")
elif marks<=59 and marks>=45:
    print("Your grade is c")
elif marks<=44 and marks>=0:
    print("You are fail")
else:
    print("Invalid Marks")

#age checker
age = int(input("Enter Your age : "))
if age>0 and age<=2:
    print("infant")
elif age>=3 and age<=18:
    print("minor")
elif age>=19 and age<=50:
    print("adult")
elif age>=51 and age<=70:
    print("senior")
else:
    print("super senior")