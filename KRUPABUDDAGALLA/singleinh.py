
#single inheritance

class Parent:
    def func1(self):
        print("this is parent class")
class Child(Parent):
    def func2(self):
        print("this is child class")

obj=Child()  #object should be created for the child class only
obj.func2()
obj.func1()

