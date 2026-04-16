num = int(input("Enter number: "))
temp = num

# count digits
count = 0
t = num
while t != 0:
    t = t // 10
    count += 1

# calculate sum
sum = 0
while temp != 0:
    rem = temp % 10
    sum += rem ** count
    temp = temp // 10

# check Armstrong
if sum == num:
    print(num, "is Armstrong number")
else:
    print(num, "is not Armstrong number")