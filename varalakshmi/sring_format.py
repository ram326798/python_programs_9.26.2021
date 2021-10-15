#Any double quotation marks within the string will need to be escaped with a backslash (\):
"""
s1="My teacher said \"Don't forget your homework.\""
print(s1)
"""

# single-quoted strings you will need to escape any apostrophes or single-quote with single backslash infront of apostrophes(\):
"""
s1='i can\'t take it'
print(s1)
"""
# using square brakets with denoting index is used for taking sub string:
"""
s1= 'hello world'
s2= "Python Programming"

print ("s1[0]: ", s1[0]) 
print ("s2[0:5]: ", s2[0:5])
"""
"""
firstName=input("enter first name:")
lastName=input("enter last name:")
profession=input("enter profession:")
dateofbirth=int(input("enter date of birth:"))
txt="user ID {0} {1} with password {3} and profession is {2}."
print(txt.format(firstName,lastName,profession,dateofbirth))
"""
"""
firstName=input("enter first name:")
lastName=input("enter last name:")
profession=input("enter profession:")
dateofbirth=int(input("enter date of birth:"))
salary=int(input("enter salary:"))
txt="user ID {lname} {fname} with password {dob} and profession is {prof} and salary is {sal:.2f}."
print(txt.format(lname=lastName,fname=firstName,dob=dateofbirth,prof=profession,sal=salary))
"""
"""
firstName=input("enter first name:")
lastName=input("enter last name:")
profession=input("enter profession:")
dateofbirth=int(input("enter date of birth:"))
print(f"user id {lastName} {firstName} with password {dateofbirth} and profession is {profession}.")
"""