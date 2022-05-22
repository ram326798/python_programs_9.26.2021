from datetime import datetime

from django.urls import clear_script_prefix

name=input("Enter your name:")

#list of items

lists='''
Rice   Rs 20/kg
salt   Rs 30/kg
sugar  Rs 40/kg
oil    Rs 20/kg
Boost  Rs 05/kg
Dal    Rs 07/kg 
'''
#declarataion
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items in dictionary format

items={'rice':20,
'salt'   : 30,
'sugar' :  40,
'oil'    : 20,
'Boost'  : 5,
'Dal'    : 7
}

#conditions using if loop

option=int(input("for list of items press 1:"))
if option== 1:
   print(lists)

#for loop for caluclation
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit: "))

    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("enter your quantity:"))
        
        if item in items.keys():

           price=quantity*(items[item])
           pricelist.append((item,quantity,items,price))
           totalprice+=price
           ilist.append(item)
           qlist.append(quantity)
           plist.append(price)
           gst=(totalprice*5)/100
           finalamount=gst+totalprice
        else:
            print("sorry ,your entered item is not available")   

    else :  
        print("you entered wrong number")

#bill generation        
inp=input("Can i bill the items yes or no :")
if inp=='yes':
    pass
    if finalamount!=0:
        print(25*"- ", "kiran supermarket", 25* "-")
        print(28*" ","wanaparthy")
        print("name.",name,30*" ","Date",datetime.now())
        print(75*"-")
        print("sno",12*" ",'items',8*" ",'Quantity',10*" ",'price')

        for i in range(len(pricelist)):
            print(i,6*" ",8*" ",ilist[i],8*" ",qlist[i],16*" ",plist[i])
            print(75*"-")
            print(50*" ",'totalamount:','Rs',totalprice)
            print('gst amount ', 50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount: ','Rs',finalamount)
            print(75*"-")
            print(25* " ","thanks for visting")
            print(75*"-")












