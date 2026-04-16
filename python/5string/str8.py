name = input("Enter string : ")
mid = len(name)//2
first_part = name[:mid]
second_part = name[mid:]
final = second_part + first_part
print(final)