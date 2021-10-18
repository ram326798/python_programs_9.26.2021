
class MyName:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def description(self,user_name="persons name"):
        return f"{user_name} is {self.lastname}  {self.firstname}"
firstname=input("enter first name:")
lastname=input("enter last name:")
m=MyName(firstname,lastname)
print(m.description())
"""
class MyName:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    def description(self,user_name="person name"):
        return f"{user_name} is {self.lastname}  {self.firstname} with age {self.age}"
m=MyName("varalakshmi","ummadisetti",20)
print(m.description())
"""