#num is divide by 5
num = int(input("Enter number "))
if num/5==0:
    print(f"{num} is divisable by 5")
else:
    print(f"{num} isn't divisable by 5")

#simple interest (p*r*n/100)
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
n = float(input("Enter Time: "))
si = (p * r * n) / 100
print("Simple Interest =", si)  

#Convert celcisus to fenhiet
# f = float(input("Enter temperature in Fahrenheit: "))
# c = (f - 32) * 5/9
# print("Temperature in Celsius =", c)
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit =", f)

#Accept radius from user and find area of circle.
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area of Circle =", area)
