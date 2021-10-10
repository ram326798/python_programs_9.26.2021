"""
l = ["pavan",23,"kumar"]
print("list is : ",l)
l2=l.copy()
print("new list ",l2)
l1 = list(l)
print("newlist l1:",l1)
"""
l1=["pavan","kumar","chimmani",23]
l2=["powerfull","people makes ","places powerfull"]
#new_list = l1+l2
print("before concatinating :",l1)
"""
for val in l2:
    l1.append(val)
print("After concatinating :"l1)
"""
l1.extend(l2)
print("After concatinating",l1)
