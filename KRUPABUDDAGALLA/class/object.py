class Myclass:
    def __init__(self,name1,name2):
        self.name1=name1
        self.name2=name2
    def myfunc(self):
        print("first student is" + self.name1)

student=Myclass("krupa","gasdil")  
print(student.name1)
print(student.name2)
student.myfunc()
student.name2="hanna"
print(student.name2)

   