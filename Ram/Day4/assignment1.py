amount=int(input("Enter amount :"))
balance=10000
if(amount!=0):
    if(amount>0):
        credited_amount=amount
        balance=credited_amount+amount
        print("Balance : ",balance)
        print("credited_amount : ",credited_amount)
    elif(abs(amount)<balance):
        debited_amount=abs(amount)
        balance-=debited_amount
        print("Debited Amount :",debited_amount)
        print("balance Amount :",balance)
    else:
        print("you have eceeded your limit")
else:
    print("Please enter a valid amount")
