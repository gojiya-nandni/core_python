lst_num = [11,34,67]
print(f"Before append list {lst_num}")
lst_num.append(90)
print(lst_num)
# print(f"Before append list {lst_num}")
# print(f"after append list {lst_num}")
lst_num1 = [56, 78]
lst_num.append(lst_num1)
print(lst_num)
lst_num.extend(lst_num1)
print(lst_num)
#insert pop remove