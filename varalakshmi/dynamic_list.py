# create a dynamic list using for loop and append method
"""
l=[True,"lakshmi","Bank","Text",10,"Credit"]
print("List :",l)
print("List length :",len(l))
l.append("pen")
for i in l:
    print("List length :",len(l))
    print("List index :",i)
    print("List Type:",type(l))
"""
l=[]
for i in range(5):
    l.append(input("enter value :"))
print("List l :",l)
print("type of List l :",type(l))
print("length of List l :",len(l))