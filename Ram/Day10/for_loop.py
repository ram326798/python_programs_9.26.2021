#break statement in for loops
"""
l=['arjun','rajni','surya']
for x in l:
    if x=='rajni':
        break
    print("list :",x)
"""
#Continue statement in for loop
"""
l=['arjun','rajni','surya']
for x in l:
    if x=='rajni':
        continue
    print("list :",x)
"""
#Range function
"""
for x in range(2,10,2):
    # print("values ",x)
    print(x,end=",")
"""
#reversing range function using step at negative
"""
for x in range(10,0,-2):
    print("values ",x)
"""
#For else condtion
"""
for x in range(5):
    print("values :",x)
else:
    print("Loop is finished")
"""
#pass statement
for x in range(10):
    pass