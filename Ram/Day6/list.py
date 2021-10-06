#iterating list using for loop w.r.t values
"""
l=["ram",10,30,True,"Krish"]
print("List :",l)
for x in l:
    print("List values :",x)
"""
#iterating list using for loop w.r.t index
"""
l=["ram",10,30,True,"Krish"]
print("List :",l)
for i in range(len(l)):
    print("List length :",len(l))
    print("List index :",i)
    print("List values :",l[i])

"""

#iterating list using while loop

l=["ram",10,30,True,"Krish"]
print("List :",l)
i=0
while i<len(l):
    print(l[i])
    i+=1
