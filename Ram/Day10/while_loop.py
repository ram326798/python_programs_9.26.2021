#Natural numbers
num=int(input("enter a number :"))
"""
i=1
while i<=num:
    print("i :",i)
    i+=1
"""
#Break statement
"""

while i<=num:
    print("i :",i)
    if(i==25):
        break #used to stop loop forcefully if condition becomes true
    i+=1
"""
#continue statement
"""
i=0
while i<=num:
    i+=1
    if(i==5):
        continue #used to skip at speicifc number if condition becomes true
    print("i :",i)
"""
#while else statement
i=1
while i<=num:
    print("i :",i)
    i+=1
else:
    print(f"Natural number are printed upto {num}")