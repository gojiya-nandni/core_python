num = int(input("Enter number "))
num1=num
count = 0
while num!=0:
    rem=num%10
    print("num==",num)
    print("rem== ",rem)
    count+=1
    num=num//10
print(f"{num1} contain {count} digits")