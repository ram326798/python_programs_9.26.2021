class Father:
    def func1(self):
        print("this is father class")

class Mother:
    def func2(self):
        print("this is mother class")     

class Child(Father,Mother):    
    def func3(self):
        print("this is child class")   

object=Child()
object.func1()
object.func2()
object.func3()           