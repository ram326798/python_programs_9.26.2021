#Creating  tuple
"""
t=("Ram",25,True)
print("type of t :",type(t))
t1=tuple(("ram",30,False))
print("type of t1 :",type(t1))
print("accesing 25 from tuple :",t[1])
print("length of t :",len(t))
print("data type of 25 in t :",type(t[1]))
ind=t.index(25)# index method use to find index of value.
print("index :",ind)
print("Using range :",t[1:])
l=list(t)   #type casting converting tuple into list to add elements
print("list :",type(l))
l.append(50)
t2=tuple(l) #type casting list into tuple
print("newly added tuple :",t2)
"""
#finding value is there or not in tuple
""""""
t=("Ram",25,True)
if 25 in t:
    print("25 is there")
else:
    print("25 is not there")
""""""