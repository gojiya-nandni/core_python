#read loops
for i in range(1, 6):
    print(i)

#year leap or not
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0):
# if (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#number is diviable by 5 & 7
num = int(input("Enter number : "))
if num/5==0:
    print(f"{num} is divisable by 5")
elif num/7==0:
    print(f"{num} is divisable by 7")
else:
    print(f"{num} is not divisable by 5 or 7") #❌

num = int(input("Enter a number: "))
if num % 5 == 0 and num % 7 == 0:
    print("Number is divisible by 5 and 7")
else:
    print("Not divisible by 5 and 7") #✔

num = int(input())
print("Divisable" if num%3==0 and num%9==0 else "not divisable")

