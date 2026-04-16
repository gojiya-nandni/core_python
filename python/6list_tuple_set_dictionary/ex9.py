emp_data={
    "name":"divya",
    "age":20,
    "incentive":[120,2500,20000],
    "salary":0
}
total_inc=0
for k,v in emp_data.items():
    if type(v)==list:
        for i in v:
            total_inc+=i

emp_data["totalinc"]=total_inc
emp_data["totalsalary"]=emp_data["salary"]+total_inc
print(emp_data)