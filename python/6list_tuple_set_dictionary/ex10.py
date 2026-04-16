dict1 = {1:0,2:0,3:0}
lst1=[2,4,6]
dict_ans={i:i*i for i in dict1.keys()}
dict_ans = {i:i*i  for i in lst1}
print(dict_ans) 

lstt1=['ahmedabad','jamnagar','broda']
dict1_ans={i:len(i) for i in lstt1}
# dict1_ans={i:i.upper() for i in lstt1}
print(lstt1)