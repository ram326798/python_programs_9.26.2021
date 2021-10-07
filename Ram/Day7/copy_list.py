#program to copy existing list into new list
"""
l=["ram",24,True,40]
print("list :",l)
l1=l.copy()
print("new list l1 :",l1)
l2=list(l)
print("new list l2 : ",l2)
"""
#program to join two lists using concatination operator
"""
l1=["ram",25,True]
l2=["krish",30,False]
new_list=l1+l2
print("new_list :",new_list)
"""
#program to join two lists using for loop
"""
l1=["ram",25,True]
l2=["krish",30,False]
print("Before concatinating l1 :",l1)
for val in l2:
    l1.append(val) 
print("after concatinating l1 list :",l1)
"""
#program to join two lists using extend method
"""
l1=["ram",25,True]
l2=["krish",30,False]
print("Before concatinating l1 :",l1)
l1.extend(l2)
print("after concatinating l1 list :",l1)
"""
#list methods
"""
append()- value will be added into list in order
clear()-to empty the list
copy()-returns a copy of existing list
count()-retuns the number of elements in a list
extend()-used to concatinate two lists
insert()-used to add element at the specific position
pop()-used to remove element at specific position
remove()-removes the value present in list
reverse()-to reverse a list
sort()-to sort list in ascending order
sort(reverse=True)-to sort list in decending order
sort(key=str.lower)-in order to sort list w.r.t case-insensitive
"""