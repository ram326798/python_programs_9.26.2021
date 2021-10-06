l = ["hi","pavan","kumar","your age is",23]
"""
print(len(l))
print(l)
print("your name is :",l[1])
print("my age is ",l[-1])

print(type(l))
print("list of specied values ",l[1:3])
print("list of specied values ",l[:3])
print("list of specied values ",l[-2:-1])
print("list of specied values ",l[-2:])
print("list of specied values ",l[:3])
print("new list is ",list(("Powerfull","people","makes","places","powerful")))
"""
name = input("Enter a name : ")
if name in l:
    print(f"{name} is in the list ")
else:
    print(f"{name} name is not found")

l[0]= "loyality"
print(l)    
print(type(l[2]))
print(len(l))
l.insert(0,"kind envolpe")
print(l)
print(len(l))