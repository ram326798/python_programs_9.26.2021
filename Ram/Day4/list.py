#list
l=["ram","hello","ram",10,10.20,True]

#indexing both in positive and negavite

# ["ram","hello","ram",10,10.20,True]
# 0		,1		,2	,3	,4		5
# -6		-5		-4	-3	-2		-1


#type(),len(),Constructor,list syntax
"""
print("List :",l[-3])
print("List :",l[3]) 
print("List of values in specified range:",l[1:4]) 
print("List of values in specified range:",l[-5:-2]) 
print("List of values from specified starting index to ending range:",l[2:]) 
print("List of values from specified ending index to starting range:",l[:2]) 
print("List length :",len(l))
print("type checking :",type(l))
print("List constructor :",list(("hello",10,20.32,True)))
print("List constructor :",type(list(("hello",10,20.32,True))))
"""
#Using membership operators
"""
name=input("Enter a name :")
if name in l:
    print(f"{name} is there in list")
else:
    print(f"{name} is not found")
"""
#inserting elements at specified index by replacing existing value in list
"""
print("List :",l)
l[2]="krish"
print("new list :",l)
"""
#inserting elements at specified range by replacing existing value in list

#how to replace elements in a list
"""
print("List :",l)
print("List :",len(l))
l[1:4]=[]
print("new List :",l)
print("List :",len(l))
print("List :",type(l[-2]))
"""

#inserting elements at specified index without replacing any value in list
"""
print("list :",l)
print("length of list :",len(l))
l.insert(2,"Hari")
print("new list : ",l)
print("new list length: ",len(l))
"""
# adding elements using append method

"""
print("list :",l)
print("length of list :",len(l))
l.append("Hari")
print("new list : ",l)
print("new list length: ",len(l))
"""
#combining two lists using extend method
"""
print("list l:",l)
print("length of list :",len(l))
l1=["hello","extends","insert","append"]
print("new list l: ",l1)
print("new list length: ",len(l1))
# l.extend(l1)
l=l+l1
print("new list :",l)
print("new list length:",len(l))
"""
#removing element from a list using remove() method w.r.t values
"""
print("list l:",l)
print("length of list :",len(l))
l.remove(10) #remove method works with value if value is there it will remove else throws error
print("new list l: ",l)
print("new list length: ",len(l))
"""

#removing element from a list using remove() method w.r.t index position
#opposite to append if pop is empty
"""
print("list l:",l)
print("length of list :",len(l))
l.pop(4) #remove method works with/without index if index is there it will remove else remove last value
l.pop()# removes last element in a list
print("new list l: ",l)
print("new list length: ",len(l))
"""

#Removing element using del keyword
"""
print("list l:",l)
print("length of list :",len(l))
del l[2] #remove method works with/without index if index is there it will remove else remove last value
del l #deletes entire list
print("new list l: ",l)
print("new list length: ",len(l))
"""

#clearing list using clear method
"""
print("list l:",l)
print("length of list :",len(l))
l.clear()
print("new list l: ",l)
print("new list length: ",len(l))
"""
"""
print("list l:",l)
print("length of list :",len(l))
for i in range(3,len(l)):
    print("i value",i)
    # print(l.pop(i))
    l.pop(3)
print("new list l: ",l)
print("new list length: ",len(l))
"""