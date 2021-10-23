#write a program to print odd number using for loop and while loop upto 20
"""a=int(input("enter a number"))
for i in range(1,a,2):
    if i==21:
        break
    print(i)"""
#using while loop
"""a=int(input("enter a number"))
i=0
while i<=a:
    i+=1
    if i==21:
        break
    print(i)"""
#write same program and skip element 10 from the loop 
"""a=int(input("enter a number"))
for i in range(1,a,2):
    if i==21:
        break
    if i==10:
        continue
    print(i)"""
#using while loop
"""a=int(input("enter a number"))
i=0
while i<=a:
    i+=1
    if i==21:
        break
    if i==10:
        continue
    print(i)"""


#write same program and stop when loop sees value 10 
"""a=int(input("enter a number"))
for i in range(1,a,2):
    if i==10:
        break
    print(i)"""
#using while loop
"""a=int(input("enter a number"))
i=0
while i<=a:
    i+=1
    if i==10:
        break
    print(i)"""


#15.3 write same program and show message "program is completed" Once loop iteration is done
"""a=int(input("enter a number"))
for i in range(1,a,2):
    if i==21:
        break
    print(i)
print("program is completed")"""

#using while loop
"""a=int(input("enter a number"))
i=0
while i<=a:
    i+=1
    if i==21:
        break
    print(i)
print("program is completed")"""
