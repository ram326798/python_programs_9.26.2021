# write a program to given alphabet is vowel or not(if else):
"""
alphabet=str(input("enter a alphabet letter(a-z):"))
if alphabet=='a' or alphabet=='e' or alphabet=='i' or alphabet=='o' or alphabet=='u':
    print("given alphabet is vowel")
    
else:
    print("given alphabet is not vowel")
"""

#write a program on calculating average marks in all subjects(nested if):
"""
telugu=int(input("enter telugu marks:"))
Hindhi=int(input("enter hindhi marks:"))
english=int(input("enter english marks:"))
maths=int(input("enter maths marks:"))
physics=int(input("enter physics marks:"))
science=int(input("enter science marks:"))
social=int(input("enter social marks:"))
total_marks=telugu+Hindhi+english+maths+physics+science+social
average_marks=total_marks/7
print("total marks:",total_marks)
print("average marks:",average_marks)
if (average_marks>=0 and average_marks<=100):
    if (average_marks>90 and average_marks<=100):
        print("you are passed in first class")
    elif (average_marks>80 and average_marks<=90):
        print("you are passed in second class")
    elif (average_marks>70 and average_marks<=80):
        print("you are passed in third class")
    elif (average_marks>=0 and average_marks<=35):
        print("you are failed")
    else:
       print("you are just passed")    
else:
    print("enter valid marks")
"""