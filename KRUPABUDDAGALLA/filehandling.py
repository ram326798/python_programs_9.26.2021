"""f=open('textfile.txt','r')
content=f.read()
print(content)
f.close()
"""


"""
f=open('textfile.txt','w')
content=f.write("this is also a write file")
print(content)
f.close()

f=open('textfile.txt','r')
content=f.read()
print(content)
f.close()
"""

f=open('textfile.txt','a')
content=f.write('this is appended')
print(content)
f.close()

f=open('textfile.txt','r')
content=f.readlines(1)
print(content)
f.close()
