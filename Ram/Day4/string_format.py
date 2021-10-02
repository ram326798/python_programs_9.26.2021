#Using simple format method

price=int(input("Enter price :"))
# txt="price of dell is {}"
# print(txt.format(price))   
# #or
print(f"price of dell is {price}")# if i give f"" i need to give variable name index and empty bracket won't be accepted


#Converting integer to float with specific round value
"""
price=int(input("Enter price :"))
txt="price of dell is {:.2f}"
print(txt.format(price))
"""
#Assigning variables using keys
"""
price=int(input("Enter price :"))
quantity=int(input("Enter Quantity :"))
itemName=input("Enter Item Name :")
txt="price of {item} is {pri} and quantity required is {quan}"
print(txt.format(pri=price,quan=quantity,item=itemName))
"""

#Multiline string using doc strings
# s1="""Hi Welcome coding world 
#       you are coding python"""
# print("S1 string :",s1)
"""
#variables assigning using index position
price=int(input("Enter price :"))
quantity=int(input("Enter Quantity :"))
itemName=input("Enter Item Name :")
txt="price of {2} is {0} and quantity required is {1}"
print(txt.format(price,quantity,itemName))
"""