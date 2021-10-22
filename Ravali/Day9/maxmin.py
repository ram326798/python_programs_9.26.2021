#11.Write a program to eliminate duplicate elements and print the output in decending order.

#decending order with removing duplicate elemnts
"""lis=[90,90,67,0,87,63,76,54,32,12,54]
final_list=[]
for i in lis:
    if i not in final_list:
        final_list.append(i)
        a=sorted(final_list)
print(a)
print("final one",a[::-1])"""
#16.write a program to find maximum in a list using for loop and if condition.
#max value in  a list
"""lis=[90,67,0,87,63,76,54,32,12,54]
final_list=lis[0]
for i in lis:
    if i>final_list:
        final_list=i
        #a.append(i)
print("max one",final_list)"""
#*****************************
#********minvalue in a list
"""lis=[90,67,0,87,63,76,54,32,12,54]
final_list=lis[0]
for i in lis:
    if i<final_list:
        final_list=i
        #a.append(i)
print("min one",final_list)"""
#17write a program to print duplicate elements in a list.
#duplicate values in a list
#***********duplicate values from a list
"""lis=[90,67,0,87,63,90,76,54,32,12,54]
#final_list=lis[0]
a=[]
for i in lis:
    if i not in a:
        a.append(i)
        #a.append(i)
    else:
        print(i,end=" ")
print("removing duplicate values from a list",a)"""



    
