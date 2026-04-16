# indexing means inside []
# slicing means seprated by :
name = input("Enter string : ")
# print(name[0])
# print(name[len(name)-1])
# print(name[1:len(name)-1])
string1 = len(name)//2
print(name[0:string1])
# print(name[0:(len(name))])
string2 = name[len(name)//2:]
final = string1 + string2
print(final)