# open() function is a key function when working with files
# open()function excpects mandatory file name exceptional mode
# r-to read a file
# a-to append a file
# w-to write a file
# x-to create a file
# modes
# ~~~~~
# t-text mode
# b-binary mode

"""
# f = open("Ram\Day17\demo.txt")    #opening a file
# or
f = open("Ram\Day17\demo.txt", "r") #specifically mentioning operation to perform
# f = open("test.txt", "r")
# f = open("C:\\Users\\760167\\lambda_task.txt", "r")
# print(f.read())   #To read all the lines
# print(f.read(6))  #to read certain characters
print(f.readline(6))    #To read certain characters if we use number in readline method
print(f.readline()) #To read a line in text file

f.close()
"""
#writing data into files
"""
f = open("Ram\Day17\demo.txt", "w")     #writing operation on file
f.write("Adding new file into demo")    #Erasing data exists in a file and adding new  content
f.close()   #closing file
f = open("Ram\Day17\demo.txt", "r") #reading operation on file
print(f.read())         #reading entire file
f.close()
"""

#appeneding data into files
"""
f = open("Ram\Day17\demo.txt", "a")     #appending operation on file
f.write(" Adding new file into demo")    #adding data into a file 
f.close()   #closing file
f = open("Ram\Day17\demo.txt", "r") #reading operation on file
print(f.read())         #reading entire file
f.close()
"""
#how to delete a file

"""
import os       # order to delete a file or folder in your machine need to import os
# if os.path.exists("Ram\Day17\demo.txt"):    #before deleting checking file is there or not
#     os.remove("Ram\Day17\demo.txt")         #to remove a file
# else:
#     print("File not found")
# os.rmdir("Ram\dummy")
"""
#creating file using write  method

# f = open("Ram\Day17\demo.txt", "w") # w operation -if file is there it will overwrite the file. If not it will create a file
# f.write("""Hi Ram how was your day  
# It been long time we went for movie
# let's go to movie""") #write method is used to write content
# f.close()
# f = open("Ram\Day17\demo.txt", "r")
# print(f.read())
# f.close()

#reading file and printing output using for loop
"""
f = open("Ram\Day17\demo.txt", "r")
for x in f:
    print(x)

"""