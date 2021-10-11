# Function is a block of code which will execute at the time of calling
# no parameter/argument function
"""
def first_function():
    a = int(input("Enter a value :"))
    b = int(input("Enter b value :"))
    c = a**b
    return c

print(first_function())
"""
# Parameterized function with positional arguments
"""
def para_function(Hero,salary):
    return Hero,salary

print(para_function("Rajni",300000))
"""
# parameterized function with dynamic arguments
"""
def para_function(*args):
    return args[1],args[0]

print(para_function("Rajni",300000))
"""
# parameterized function taking dynamic dictionary values
"""
def para_function(**kwargs):
    return kwargs['salary'],kwargs['Hero']

print(para_function(Hero='Rajni',salary=300000))
"""
# parametrized function with default values
"""
def para_function(Hero='Rajni'):
    return Hero
print(para_function())
"""
# passing list into function
"""
def list_function(l):
    return l
l=[1,2,3,2,'ram']
print(list_function(l))
"""
