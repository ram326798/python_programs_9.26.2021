#hybrid inheritance

class A:
    def __init__(self):
        print("This is class A")

class B(A):
    def __init__(self):
        print("this is class B") 
        super().__init__() #super is a keyword that is used to print the above parent class output
obj=B()              