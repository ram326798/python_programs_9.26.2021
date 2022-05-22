


class Myclass:
    def __init__ (self,name,age):
       self.name=name
       self.age=age
    def myfunc(self):
      print("his particular age is"+ self.age)
   

person1=Myclass("harathi","30")
print(person1.name)
print(person1.age)    
person1.myfunc()          