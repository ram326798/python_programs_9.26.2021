age=int(input("Enter age "))
if(age>0):
    if(age<18):
        print("Given person is minor")
    elif(age>=18 and age<25):
        print("Given person is Young age")
    elif(age>=25 and age<60):
        print("Given person is middle age")
    else:
        print("Given person is old age")
else:
    print("Enter a positive number")