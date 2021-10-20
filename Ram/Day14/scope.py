#if we declare a variable outside a method or class we can access at all inner stages as it is a global variable
#If a variable is declared inside a method or class we cannot access outside of that method or class until it is declared as global

def Zoo():
    global speed
    speed=60
    print("inside Zoo speed",speed)

Zoo()
print("outside speed",speed)
