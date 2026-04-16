# rows = 4

# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * i)


num = int(input("Enter number"))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        if j <= num - i:
            print(" ", end="")
        else:
            print("*", end="")
    print()