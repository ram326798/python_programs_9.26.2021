age=int(input("Please Enter Your age: "))
if(age>0):
    if(age<18):
        print("You are Minor")
    elif(age>=18 and age<=25):
        print("You are in Young age")
    elif(age>=25 and age<=60):
        print("You are in Middle age")
    else:
        print("You are in Old age")
else:
    print("Please enter correct age value")
