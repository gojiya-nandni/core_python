city = ['jamnagar', 'ahmedabad', 'mumbai', 'rajkot', 'surat']

# city.sort()
# print(city)
# city.sort(reverse=True)
# print(city)
# city.sort(key=len)
# print(city)

for i in range(len(city)):
    print(i,city[i]) #print list with index

c_name = input("Enter city name ")
# if c_name in city:
if city.count(c_name)>0:
    print(f"{c_name} is in list")
else:
    print(f"{c_name} is not in list")

for i in city:
    if i==c_name:
        print(f"{c_name} is available in list")
        break
else:
    print("{c_name} is available in list")