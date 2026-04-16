student_data = {
    "name":"nandini",
    "c_no":1234554321,
    "marks":[120,20,40]
}
# print(student_data.items())
total=0
for k,v in student_data.items():
    # print(k)
    if type(v)==list:
        for i in v:
            total+=i
        print("\t",total)