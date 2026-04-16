marks = int(input("Enter marks: "))

if marks >= 0 and marks <= 105:   # valid range
    
    if marks >= 70:
        print("A Grade")
    
    else:
        if marks >= 60:
            print("B Grade")
        
        else:
            if marks >= 45:
                print("C Grade")
            
            else:
                print("Fail")

else:
    print("Invalid marks")


#age & weight for blood donate
age = int(input("Enter Your age"))
weight = int(input("Enter Your weight"))
if(age>=18 and weight>=55):
    print("Eligilbe to donate blood")
else:
    print("Not Eligilbe to donate blood")
  