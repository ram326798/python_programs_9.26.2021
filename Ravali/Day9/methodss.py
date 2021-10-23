#write a program to call parent class methods and variables in child class
"""class Parent:
    def display(self,bankname,ifsccode,area):
        self.bankname=bankname
        self.ifsccode=ifsccode
        self.area=area
class Child(Parent):
    def show(self,bankname,ifsccode,area):
        print(f"the bank name is {bankname} and {ifsccode} area  is{area}")
a=Child()
a.show("sbi","sci123","knr")"""

#13.write a program to getting selling price using lambda function. Note selling price=profit-buying price
def cost(price):
    return lambda c:price+b


#a=int(input("enter a buying price"))
b=int(input("enter profit"))
#x=lambda a,b:b+a
bp=cost(200)
print("selling price",bp(2))