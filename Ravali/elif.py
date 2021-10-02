age=int(input("Enter age "))
if(age>0):
    if(age>0 and age<=13):
        print("you are a child")
    elif(age>14 and age<=18):
        print("You are teenager")
    elif(age>=18 and age<25):
        print("You are Young ")
    elif(age>=25 and age<60):
        print("Given person is middle age")
    else:
        print("senior citizen")
else:
    print("Enter a correct number")