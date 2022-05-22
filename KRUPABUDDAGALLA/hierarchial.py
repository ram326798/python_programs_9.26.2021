class Parent():
    def func1(self):
        print("this is parental class")

class Child1(Parent):
    def func2(self):
        print("this is child1 class")    

class Child2(Parent):
    def func3(self):
        print("this is child2 class")

obj=Child2()

obj.func1()
#obj.func2()
obj.func3()                    