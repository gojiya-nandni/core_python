for i in range(10):
    print("Hello World")

for i in range(1000, 0, -100):
    # print(i)
    print(i, "-", i - 99)

for i in range(0,100,2):
    print(i)

for i in range(100):
    if i%2==0:
        print(f"{i} is Even number")
    else:
        print(f"{i} is Odd number")

a = 5
for i in range(11):
    print(f"{a}*{i}={a*i}")

for i in range(10):
    if i==6:
        break
    print(i)

for i in range(5):
    if i==2:
        continue
    print(i)

for i in range(3):
    if i==4:
        pass
    print(i)        

i = 1
while i <= 5:
    print(i)
    i += 1

i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i <= 3:
    pass
    i += 1