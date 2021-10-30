# map is used to perform operation on all the elements in a input list.
# syntax
# map(function to apply,list_of_imputs)

# normal procedure
"""
l=[1,2,3,4]
sq=[]
for i in l:
    sq.append(i*2)
print(sq)
"""

# using map in multiplication

"""
l=[1,2,3,4]
sq=list(map(lambda x:x*2,l))    #list will be written
# sq=[map(lambda x:x*2,l)]    #list object will be written
print("map procedure",sq)
"""

# using map in fucntions
"""
def mul(x):
    return (x*x)
def add(x):
    return (x+x)
func=[mul,add]
for i in range(5):
    v=list(map(lambda x:x(i),func))
    print(v)
"""

# Filter uses to perform filtering based on condition
# syntax
# filter(function to apply,list_input)
"""
l = [-1, -2, -3, 0, 1, 2, 3, 4]
neg = list(filter(lambda x: x < 0, l))
print("negative numbers : ", neg)
"""

# reduce applies to sequential pairs of values in a list and produces single output
# syntax
# reduce(funtion to apply,list_input)

# normal procedure
"""
prod=1
l=[1,2,3,4]
for num in l:
    prod=prod*num

print("product of n numbers : ",prod)
"""

# using reduce procedure

from functools import reduce
l = [1, 2, 3, 4]
prod = reduce(lambda x, y: x*y, l)
print(prod)
