#How to reverse a list
"""
l=["ram",10,30,True,"Krish"]
l=l[::-1]
print(l)
"""

#List comprehension
# syntax
# newlist=[expression for item in list if condition==True]
"""
l=["ram","Kiwi","apple","banana","Krish"]
l2=[x for x in l]
print("l2 :",l2)
newlist=[x for x in l if "r" in x]
print("new list :",newlist)
[print("printing using index :",l[x].upper()) for x in range(len(l))]
[print("printing using index :",l[x].lower()) for x in range(len(l))]
"""
#list comprehension using if else
"""
l=["ram","Kiwi","apple","banana","Krish"]
newlist=[x if x!="apple" else "banana" for x in l]
# for x in l:
#     if x!="apple":
#         print("x :",x)
#     else:
#         print("banana")
print("new list :",newlist)
"""

l=["ram","krish","Apple","animal"]
# l.sort(key=str.lower)#used to sort list w.r.t case insensitive.
# l.sort()#used to sort list 
# l.sort(reverse=True)#used to reverse list after sorting
l.reverse()# used to reverse list without sorting 
print("sorted list",l)