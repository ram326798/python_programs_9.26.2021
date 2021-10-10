"""s1={5,6,5,"hyd","pune",89.0,True}
print(s1)
for i in s1:
    print(i)"""
# value is there or not
"""s1={5,6,5,"hyd","pune",89.0,True}
if 6 in s1:
    print("is there")
else:
    print("not foud")"""

# add values to set
"""s1={5,6,5,"hyd","pune",89.0,True}
s1.add(9)
print(s1)"""

#concate 2 sets 
"""s1={5,6,5,"hyd","pune",89.0,True}
s2={5,6,5,"hyd","pune",89.0,True,"delhi",78.9}
#s1.update(s2) will ot take 3rd variale to assign
s3=s1.union(s2)# takes 3rd variale to assign
print(s3)"""
# set methods
"""s1={5,6,5,"hyd","pune",89.0,True}
s2={5,6,5,"hyd","pune",89.0,True,"delhi",78.9}
s3=s2.difference(s1)#difference returns the objects which gives the differece of s2 object with s1
print(s3)
s4=s3.copy()
print(s4)"""
# discard,remove
s1={5,6,5,"hyd","pune",89.0,True}
s2={5,6,5,"hyd","pune",89.0,True,"delhi",78.9}
s1.discard(9)#value is not thr also ,will ot throw error
s2.remove(5)# throws error
s2.pop()#will ot take any arguements
print(s2)


