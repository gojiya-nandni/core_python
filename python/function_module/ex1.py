def student_detail(rollno,name,age):
    print(f"{rollno}-{name}-{age}")
student_detail(1,"shivam",21)
student_detail(2,"jay",20)

r=int(input("Enter rol no "))
n=input("Enter Name ")
a=int(input("Enter age "))
student_detail(r,n,a)