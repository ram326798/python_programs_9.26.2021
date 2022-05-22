#multilevel inheritance

class Parent:
    def func1(self):
      print("this is parental class")

class Child(Parent):
    def func2(self):
        print("this is child class")   

class Grandchild(Child):
    def func3(self):
        print("this is grandchild class")       

obj=Grandchild() #object should be created for the grandchild class
obj.func1()
obj.func2()
obj.func3()

