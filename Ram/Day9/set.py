#Set is unordered and unindexed .
#so we cannot change set values or access values using index. But we can add values
"""
s={1,21,2,2,"ram","ram"}
print("len :",len(s))
print("type :",type(s))
for x in s:
    print("set :",x)
"""

#Set constructor
"""
l=[1,2,3,4,2,"ram",True,30.6]
print("list :",l)
s=set(l)
print("set : ",s)
s1=input("enter a value :")
if s1 in s:
    print(f"{s1} is present")
else:
    print(f"{s1} is not there")
"""
#Adding items in set
"""
s={1,2,3,"ram",2,3,5}
print("set : ",s)
s.add("krish")
print("new set :",s)
"""
#concatinating two sets 
"""
s1={1,2,3,"ram",2,4,5}
print("set 1 :",s1)
s2={1,2,3,4,"krish"}
print("set 2 :",s2)
s1.update(s2)
print("new set :",s1)
"""
#interseting two sets
"""
s1={1,2,3,"ram",2,4,5}
print("set 1 :",s1)
s2={1,2,3,4,"krish"}
print("set 2 :",s2)
s3=s1.intersection(s2)
print("new set :",s3)
"""
#removing element from set
"""
s1={1,2,3,"ram",2,4,5}
print("set 1 :",s1)
s1.remove(2)#if value is not there remove will raise an error
s1.discard(6)#if value is not there if will go with flow without raising error
print("new set :",s1)
print("removed value from set :",s1.pop())#pop will remove last item in a set
s1.clear()
print("After clearing set :",s1)
del s1
print("after deleting set :",s1)# this will raise error as s1 set is deleted
"""
#union of sets
"""
s1={1,2,3,"ram",2,4,5}
print("set 1 :",s1)
s2={1,2,3,4,"krish"}
print("set 2 :",s2)
s3=s1.union(s2)
print("Union s3 :",s3)
"""
#intersetion_update method in set
"""
s1={1,2,3,"ram",2,4,5}
print("set 1 :",s1)
s2={1,2,3,4,"krish"}
print("set 2 :",s2)
s1.intersection_update(s2)
print("intereseting values in s1:",s1)
"""
#symetric_difference_update method works opposite to intersection
s1={1,2,3,"ram",2,4,5}
print("set 1 :",s1)
s2={1,2,3,4,"krish"}
print("set 2 :",s2)
s1.symmetric_difference_update(s2)
print("intereseting values in s1:",s1)