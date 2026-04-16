# email = input("Enter email")
# print(email.endswith("@gmail.com"))

# num = input("Enter Your Mobile Number ")
# print(num.startswith("91 "))

num = int(input("Enter Your Mobile Number "))
num1 = str(num)
if num1.startswith("91 ") and len(num1)==12:
    print(f"{num1} is valid contact number")
else:  
    print(f"{num1} is not valid contact number")