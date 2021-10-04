#4.write a program to find **"Rajni" using in** a list.
"""
l= [100,"lakshmi","priya","rajini",True,]
ds=input("Enter a value :")
if ds in l:
    print(f"{ds} is there in list") 
else:
    print (f"{ds} is not their in list")

"""

#5.Write a program to replace ["Hello","world",45,503.24,True] to ["Thank you"]
"""
l=["Hello","world",45,503.24,True]
print("list:", l) 
l[0:5]=["Thank you"]
print(" new list:", l)
"""

#dynamic string
# 3.Write a program to give dynamic string.
# Note: 1.String should be **"{persons} went to {Movie_name} at {theatre_name}"**
"""
person = input ("Enter Person Name:")
movie_name = input ("Enter Movie Name:") 
theatre_name = input ("Enter Theatre Name:")
txt = "{person} went to {movie_name} movie at {theatre_name} theatre"
print(txt.format(person=person, movie_name=movie_name, theatre_name=theatre_name))
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
#6.write a program to create new list with existing value.
# Note:from **li=["apple","bird",True,33]** to **new_li=["bird",True,33]**
"""
li=["apple","bird",True,33]
print("Old list ",li)
# li[0:4]=["bird",True,33]
# or
# li.remove("apple")
# or
li.pop(0)
print("new list ",li)
"""

# 7.write a program to check whether given type is list or not. **If it is list print("given type is list") else print("given output is not list")**
"""
li=["apple","bird",True,33]
li=tuple(li)
if type(li) is list:
    print("given type is list")
elif( type(li) is set):
    print("given type is set")
else:
    print("given type is tuple")
"""
