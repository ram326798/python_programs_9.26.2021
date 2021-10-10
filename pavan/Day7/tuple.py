"""
t= ("pavan","kumar",12)
print(type(t))
t1 = tuple(("pavan",3))
print(t1)
print("Accesing kumar in tuple t :",t[1])
print("length of t :",len(t))
print("Accesing the data type of kumar in tuple t :",type(t[1]))
ind=t.index("kumar")
print(ind)
print("using range:",t[1:])
l=list(t)
print("type of :",type(l))
l.append(1997)
print("new list :",l)
l2=tuple(l)
print("type of l2 :",type(l2))
"""
t=("ram",25,True)
if 25 in t:
    print("25 is there")
else:
    print("25 is not there")    