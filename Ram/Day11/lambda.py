# lambda function is an anonymous function
# lambda arguments:expression

# lambda with two paraments
"""
arg=lambda a,b:a+b
print(arg(10,20))
"""
# Lambda function with three arguments
"""
def arg(a, b, c): 
    return a+b

print(arg(10, 20, 40))
"""
#lambda with normal function
"""
def func(n):
    return lambda a, b: a**b+n

vari = func(3)
print("Result :",vari(2, 4))

def func2(selling_price):
    return lambda buying_price:selling_price-buying_price

profit=func2(10000)
print("Result2 :",profit(3000))
"""