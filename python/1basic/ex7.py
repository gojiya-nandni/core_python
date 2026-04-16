num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))
sum = num1 + num2
# print(f"Sum of {num1} and {num2} is {sum}")
print(sum)

# arithmetic operator + - * / % // **
sub = num1 - num2
print(sub)

mul = num1 * num2
print(mul)

div = num1 / num2
print(div)

mod = num1 % num2 #module give module reminder
print(mod)

fldiv = num1 // num2 #floor division give quotient(bhagfal) 
print(fldiv)

expnt1 = num1 ** 2 #power (varg)
expnt2 = num2 ** 3
print(expnt1)
print(expnt2)

#logical operator and, or
num = int(input("Enter number : "))
if num>0 and num>=0:
    print(f"{num} is positive")

numm = int(input("Enter number : "))
if numm>0 or numm>=0:
    print(f"{numm} is positive")

#relation operator < > <= >= == !=
digit = int(input("Enter number"))
if digit!=0:
    print("Digit not zero")

#membership oprator in not in
fruits = ['banana', 'apple']
print("apple" in fruits)
print("banana" not in fruits)

#identity operator is, not is 
x = ["mango", "cherry"]
y = ["mango", "cherry"]
print(x is y) #print(x == y)
print(x is not y)

#bitwise operator &and |or ^xor ~not <<leftshift >>rightshift
print(6 & 3)
print(6 | 3)
print(6 ^ 3)