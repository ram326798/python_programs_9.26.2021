#Write a program to find whether apple is there or not using list comprehension. note:l=["sqaure","triangle","apple"]
l=["sqaure","triangle","apple"]
#using list comprehension
l2=[print("apple is thr") for x in l if x=="apple"]

for x in l:
    if x=="apple":
        print("apple is there")