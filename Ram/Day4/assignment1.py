amount=int(input("Enter amount :"))
# 1.Write a program to find credited amount,balance using **if else and operators.**
#   Note:variables:**amount,balance,credited_amount**,
#   Formula: **credited_amount=amount**,**balance+=credited_amount**,
#   **amount** should be greater than zero 

balance=10000
if(amount!=0):
    if(amount>0):
        credited_amount=amount
        balance+=credited_amount
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
