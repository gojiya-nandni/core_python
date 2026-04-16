def checknumber(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

def finfactorial(num):
    fact=1
    for i in (1,num+1):
        fact*=i
    print(fact)

f1 = int(input("Enter number "))
finfactorial(f1)