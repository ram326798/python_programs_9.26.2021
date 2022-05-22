"""def myfunc(n):
  return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))
"""
"""
x=lambda a,b: a+b
print(x(5,6))
"""
"""
x=lambda a:a*9
print(x(5))
"""


def myfunc(n):
    return lambda a:a*n
mytripler=myfunc(3)
print(mytripler(11))