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
"""
#how to replace elements in a list
print("List :",l)
print("List :",len(l))
l[1:4]=[False,10000,True,"died"]
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
