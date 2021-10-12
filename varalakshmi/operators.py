#arthimetic operators
"""
a=int(input("enter a value:"))
b=int(input("enter b value:"))
if b!=0:
    print("sum of a & b:","float value",float(a+b), "and int value" ,int(a+b))
    print("subtraction of a & b:","float value",float(a-b), "and int value" ,int(a-b))
    print("multiplication of a & b:","float value",float(a*b), "and int value" ,int(a*b))
    print("exponential of a & b:","float value",float(a**b), "and int value" ,int(a**b))
    print("division of a & b:","float value",float(a//b), "and int value" ,int(a//b))
    print("floor division of a & b:","float value",float(a/b), "and int value" ,int(a/b))
    print("modulo of a & b:","float value",float(a%b), "and int value" ,int(a%b))
"""
#comparison operators
"""
a=int(input("enter a value:"))
b=int(input("enter b value:"))
if b==a:
    print("b equals to a",b==a)
elif b>a:
    print("b is greater than a",b>a)
else:
    print("b is less than a",b<a)
"""
#assignment operators
"""
a=int(input("enter a value:"))
b=int(input("enter b value:"))
for d in range (b):
    d-=b
    print("c value",d)
"""
"""
b=int(input("enter b value:"))
for d in range (b):
    d+=b
    print("c value",d)
"""

#b=int(input("enter b value:"))
#for d in range (b):
    #d=b*2
    #print("c value",d)


#identity operators (is)
"""
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if b is a is c:
    print("b equal to a equal to c",b>a==c)
else:
    print("invalid input")

"""
#logical operators (and, or, not)
"""
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a==b and b>c:
    print("a equals to b greter than c")
else:
    print("output not worthy")
"""
"""
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a==b or b>c:
    print("given statement is valid")
else:
    print("output not worthy")
"""
"""
#.....not 
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a!=b or b>c:
    print("given statement is valid")
else:
    print("output not worthy")
"""
#membership operators (in, not in)
"""
a=["lucky","money",20,True,"baby"]
if ("lucky" in a):
    print("lucky is present")
else:
    print("lucky is not there")
"""
"""
a=["lucky","money",20,True,"baby"]
if ("lucky" not in a):
    print("lucky is not present")
else:
    print("lucky is there")
"""
#a=["lucky","money",20,True,"baby"]
#b=[1,3,4,"seetha","geetha",20]
#if (b in a):
 #   print(" is present")
#else:
 #   print(" is not there")
