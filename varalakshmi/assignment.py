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