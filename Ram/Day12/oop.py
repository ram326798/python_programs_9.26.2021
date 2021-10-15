# creating class
"""
class MovieName:
    pass
"""
# Creating object in python
"""
class MovieName:
    pass


m = MovieName()
"""
# creation of class constructor __init__
# Usage: to assign values to the variables when an object is created
# self keyword is used to create instancce of class
"""
class MovieName:
    def __init__(self,hero,villian):
        self.hero=hero
        self.villian=villian
"""
# Creation of method inside a class
"""
class MovieName:
    def __init__(self,hero,villian):
        self.hero=hero
        self.villian=villian
    def description(self,film_industry='Telugu Partners'):
        return f"{film_industry} releasing movie with hero {self.hero} and villian is {self.villian}"

m=MovieName("Prabhas",'Rana')
print(m.description())
print(m.description('Bollywood'))
"""
# syntax of Inheritance
"""
class Base_Class:
    # body of base class or parent class
    pass
class Instance_Class(Base_class):
    #body of instance class or child class and also we can access parent class methods,variables and values
    pass
"""
# Example of inheritance
"""
class Zoo:
    def __init__(self, category, food, living):
        self.category = category
        self.food = food
        self.living = living

    def description(self):
        return f"{self.category} eat {self.food} and lives in {self.living}"


class Lions(Zoo):
    def intro(self):
        return f"{self.category} is king of jungle"


z = Zoo('Lions', "meat", 'Jungle')
print(z.description())  #Accessing parent class method using parent method.
li = Lions('lioness', 'meat', 'jungle')
print("calling parent class method using child class object :", li.description()) #Accessing parent class method using child object
print("calling child class method using child class object :", li.intro())  #Accessing child method using child object.

"""