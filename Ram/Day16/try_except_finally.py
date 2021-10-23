# Syntax for try except block
"""
try:
    pass
except:
    pass
"""

#in a try except block try will excute first where we will have some conditions, if it fails it will enter into except block
"""
def division(a, b):
    try:
        result = a//b   #interger division
        print("result :",result)
    except ZeroDivisionError:
        print("you are dividing by zero please change b value ",ZeroDivisionError)    

a=int(input("enter a value :"))
b=int(input("enter b value :"))
division(a,b)
"""

#try ,except, else
"""
def division(a, b):
    try:
        result = a//b   #interger division
        
    except ZeroDivisionError:
        print("you are dividing by zero please change b value ",ZeroDivisionError)    
    else:
        print("result :",result)
a=int(input("enter a value :"))
b=int(input("enter b value :"))
division(a,b)
"""

# try, except ,  finally
"""
def division(a, b):
    try:
        result = a//b   #interger division 
    except ZeroDivisionError:
        print("you are dividing by zero please change b value ",ZeroDivisionError)  
    except Exception:
        print("some error occured apart from zero divison error ")  
    else:
        print("result :",result)
    finally:
        print("code has been run successfully/failure")
a=int(input("enter a value :"))
b=int(input("enter b value :"))
division(a,b)
"""

"""
try:
    raise NameError("Hello") #raise error
except NameError:
    print("Exception")
    raise   #whether exception was raised or not
"""

a=int(input("Enter a value :"))
if a<0:
    raise Exception("You have entered negative number") #raise keyword is used to raise an exception