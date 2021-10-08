#how to delete a tuple
"""
t=("ram","apple",10,True)
print("tuple :",t)
del t
print("tuple deleted")
"""
#concatinating two tuples
"""
t1=("ram","apple",10,True)
t2=("concatinate","l1")
t3=t1+t2
print("T1 :",t1)
print("T2 :",t2)
print("T3 :",t3)
"""

#Dynamic arguments *variablename
"""
t=("ram","krish",25,"Hello",30)
a,*b,c=t
print("A :",a)
print("B :",b)
print("C :",c)
"""
#Arthemetic operation
"""
a,b,c=10,20,30
d=a+b+c
print("sum of d :",d)
"""
#Unpacking tuple using for loop
"""
t=("ram","krish",25,"Hello",30)
for i in range(len(t)):
    print("tuple index :",i)
    print("tuple values :",t[i])
"""
#Unpacking tuple using while loop
"""
t=("ram","krish",25,"Hello",30)
i=0
while i<len(t):
    print("tuple :",t[i])
    i+=1
"""
#mutiplying tuple by 2 to get copy and extend values
"""
t=("ram",True,25)
t1=t2*2
print("tuple : ",t1)
"""
