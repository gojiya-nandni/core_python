#arithmetic operator
base = int(input("Enter base: "))
power = int(input("Enter power: "))
result = base ** power
# result = pow(base, power)
print("Answer:", result)

#relationship operator
a = int(input("Enter num1"))
b = int(input("Enter num2"))
print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal
print(a <= b)   # Less than or equal

#logical operator ---- and or not
a = 10
b = 5
print(a > 5 and b > 2)   # True and True
print(a > 5 and b > 10)  # True and False
print(a > 5 or b > 10)   # True or False
print(a < 5 or b > 10)   # False or False
print(not(a > 5))        # not True

#conditional stmt
age = int(input("Enter your age"))
if age>18:
    print("You are eligible for vote")
else:
    print("You aren't eligible for vote")