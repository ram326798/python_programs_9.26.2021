# Encapsulation
"""
class Zoo:
    def __init__(self, category, food, living):
        self._category = category
        self._food = food
        self.living = living

    def description(self):
        return f"{self._category} eat {self._food} and lives in {self.living}"

z = Zoo('Lions', "meat", 'Jungle')
print(z.description())  #Accessing parent class method using parent method.
"""
# Encapsulating method
"""
class Zoo:
    def __init__(self, category, food, living):
        self.__category = category
        self._food = food
        self.living = living

    def description(self):
        return f"{self.__category} eat {self._food} and lives in {self.living}"

z = Zoo('Lions', "meat", 'Jungle')
print(z.description())  #Accessing parent class method using parent method.
print(z._food) #accessing public variable
print(z.__category)
"""
# Accessing private variables outside of class
"""
class Zoo:
    def __init__(self, category, food, living):
        self.__category = category
        self._food = food
        self.living = living

    def description(self):
        return f"{self.__category} eat {self._food} and lives in {self.living}"

z = Zoo('Lions', "meat", 'Jungle')
print(z.description())  #Accessing parent class method using parent method.
print(z._food) #accessing public variable
print(z._Zoo__category) #Name mangling -Used to access private variables or methods syntax _ClassName__private method name or variable name
"""
# Polymorphism- having many forms
"""
class Benz:
    def description(self):
        print("Benz has been called")
class Ferrari:
    def description(self):
        print("Feerari has been called")
b=Benz()
f=Ferrari()
for car in (b,f):
    car.description()
"""
# Abstraction
# hiding internal details/implementation of a function
# syntax
"""
from abc import ABC #ABC-Abstract Base Class
class abs_class(ABC):
    pass
    #body of the class
"""
# can we call abstract method using object? No we can not
"""
from abc import ABC, abstractmethod  # ABC-Abstract Base Class
class abs_class(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def speed(self,x):
        pass

a=abs_class("birds")
"""
# how to call abstract methods? using inheritance

from abc import ABC, abstractmethod  # ABC-Abstract Base Class
class abs_class(ABC):
    def __init__(self, name):
        self.name = name

    def description(self):
        print(f"we are in abstract class {self.name}")

    @abstractmethod
    def speed(self, x):
        pass


class Child(abs_class):
    def speed(self, x):
        print(f"The {self.name} goes with speed {x}")
c=Child("Lions")
c.description()
c.speed("20 KM/hr")
