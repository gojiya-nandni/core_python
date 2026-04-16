i=1
while i<=10:
   print("Hello",i)
   i+=1
# print value from 10 to 20 
i=10
while i<=20:
    print(i)
    i+=1
# # print alternate value from 100 to 120
num1 = int(input("Enter start number "))
num2 = int(input("Enter end  number "))
# i = num1
while num1<=num2:
    print(num1)
    num1+= 2

i=1000
while i>=1:
    print(i)
    i-=100

num = int(input("Enter number of table : "))
if num%2==0:
    i=1
    while i<=10:
        total=num*i
        print(f"{num}*{i}={total}")
        i+=1
else:
    print("Multilication not perform ")

i=1
while i<=1000:
    if i%5==0 and i%7==0:
        print(i)
    i+=1
