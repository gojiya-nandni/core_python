# #find factorial number
# num = int(input("Enter number : "))
# fact = 1
# for i in range(1,num+1):
#     fact*=i
# print(fact)

# #sum of n num
# n = int(input("Enter number : "))
# if n>0:
#     sum = 0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
# else:
#     print(f"{n} is not natural number")

# # find prime number
# prime =  int(input("Enter number : "))
# if prime>0:
#     for i in range(2,prime):
#         if prime % i ==0 :
#             print(f"{prime} is not prime number")
#             break
#     else:
#         print(f"{prime} is prime number ")
# else:
#     print(f"{prime} is not prime number")   

# # sum of 100 even number
# num = int(input("Enter number : "))
# sum = 0
# if num %2 == 0 :
#     for i in range(num,100):
#         sum += i
#     print(sum)
# else:
#     print(f"{num} is not even number")

# # sum of numbers those divisable by 5 and 7 between 1000-2000
# num = int(input("Enter number : "))
# sum = 0
# if num%5==0 and num%7==0:
#     for i in range(1000,2000):
#         sum+=i
#     print("sum of numbers those divisable by 5 and 7 between 1000-2000 is ",sum)
# else:
#     print(f"{num} is not divisable by 5 and 7")

#count total even and odd numbers and both sum
num = int(input("Enter number : "))
even_digit = 0
odd_digit = 0
sum = 0
while num > 0:
    digit = num % 10
    sum+=digit

    if digit % 2 == 0:
        even_digit += 1
    else:
        odd_digit += 1

    num = num // 10

print("Even digits = ",even_digit)
print("Odd numbers : ",odd_digit)
print("Sum ",sum)