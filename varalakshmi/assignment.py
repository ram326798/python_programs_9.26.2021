#3.Write a program to give dynamic string.
#Note: 1.String should be **"{persons} went to {Movie_name} at {theatre_name}"**
"""
person = input ("Enter Person Name:")
movie_name = input ("Enter Movie Name:") 
theatre_name = input ("Enter Theatre Name:")
txt = "{person} went to {movie_name} movie at {theatre_name} theatre"
print(txt.format(person=person, movie_name=movie_name, theatre_name=theatre_name)) 
"""
"""
person = input ("Enter Person Name:")
movie_name = input ("Enter Movie Name:") 
theatre_name = input ("Enter Theatre Name:")
txt = "{0} went to {1} movie at {2} theatre"
print(txt.format(person,movie_name, theatre_name)) 
"""
#2.Write a program to find given number is greater than or less than or equal to 100.
"""
number = int(input("enter a number:"))
if(number>100):
    print ("Given Number is Greaterthan 100:", number) 
elif(number==100):
    print ("Given Number is Equal to 100:", number) 
else:
    print ("Given Number is Lessthan 100:", number) 
"""
#1.Write a program to find credited amount,balance using **if else and operators.**
 # Note:variables:**amount,balance,credited_amount**,
  #Formula: **credited_amount=amount**,**balance+=credited_amount**,
  #**amount** should be greater than zero 
"""
balance = float (input ( "present balance"))
amount = float (input (" enter the amount created")) 
credited_amount = amount+balance
if ( amount> 0) :
    print("Total amount ", credited_amount) 
else:
    print (" please credit a valid amount ") 
"""

#10.write a program to assign dynamic number of values in a constructor class and access it using a method.

"""
class MyName:
    def __init__(self,firstname,lastname,age,profession):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.profession=profession
    def description(self,user_name="User ID"):
        return f"{user_name} is {self.lastname}  {self.firstname} with age {self.age} and profession is {self.profession}."
firstname=input("enter first name:")
lastname=input("enter last name:")
age=int(input("enter age:"))
profession=input("enter profession:")
m=MyName(firstname,lastname,age,profession)
print(m.description())
"""
#11.Write a program to eliminate duplicate elements and print the output in decending order.
"""
l1=["lakshmi","sariyu","sarala","sariyu","lakshmi","lilly"]
print("taken list:",l1)
l2=set(l1)
print("eleminating duplicate values:",l2)
l3=list(l2)
l3.sort(reverse=True)
print("elements in decending order:",l3)
"""
a=[]
for i in range (8):
    a.append(input("enter list:"))
    print("list of a1:",a)
    a2=set(a)
    a3=list(a2)
    a3.sort(reverse=True)
    print("decending order:",a3)
#12.write a program to add values into tuple using any constructor.
#static
"""
a=("cat", "dog","rat","crow",1,8)
print("tuple of a:",a)
print("type of a:",type(a))
b=list(a)
print("lis of b:",b)
print("type of b:",type(b))
b.append("parrot")
c=tuple(b)
print("new tuple:",c)
print("type of c:",type(c))
"""
#dynamic
"""
a=()
a1=list(a)
for i in range (5):
    a1.append(input("enter list:"))
    print("list of a1:",a1)
    print("type of a1:",type(a1))
    a2=tuple(a1)
    print("tuple of a2:",a2)
    print("type of a2:",type(a2))
  """      

#13.write a program to getting selling price using lambda function.
#**Note selling price=profit-buying price**
"""
def fun(buying_price):
    return lambda selling_price:buying_price+profit   
profit=int(input("enter profit:"))
#buyig_price=int(input("enter buying price:"))
cost_price=fun(2000)
print("selling price:",cost_price(0))
"""  


