#creating dictionary
"""
d={"Hero":"Arjun",'date_of_birth':'17/12/1970','favourite_colour':"Blue",'age':50}
print("type of d: ",type(d))
print("Dictionary d: ",d)
print("age is :",d['age'])#Accessing values using key in dictionary
print("Hero is :",d.get('Hero'))#Accessing values using get method and key in dictionary
d['car']='Benz' #adding new values into dictionary
print("new Dictionary d: ",d)
d['car']='Ferrari' #changing existing value using key
print("after changing value new Dictionary d: ",d)
print("len of d: ",len(d))
print("Printing keys :",d.keys())   #getting keys from dictionary
print("Printing values :",d.values()) #getting values from dictionary
print("Printing values :",list(d.values())) #converting values of dictionary into list
print("Printing items :",d.items()) #getting key values in terms of list and tuple.
"""
#checking key is there or not
"""
d={"Hero":"Arjun",'date_of_birth':'17/12/1970','favourite_colour':"Blue",'age':50}
if "age" in d:
    print("Age key is there")
    print("Age value is :",d['age'])
"""
#checking value is there or not
"""
d={"Hero":"Arjun",'date_of_birth':'17/12/1970','favourite_colour':"Blue",'age':50}
if 'Arjun' in d.values():
    print("Arjun is present")
else:
    print("Arjun is not there")
"""
#editing or adding key values into dictionary using update method
"""

# d['age']=55
d.update({'age':55})
d.update({'salary':55000})
print("age is modified :",d['age'])
print("new dictionary:",d)
"""
#printing values using for loop
"""
d={"Hero":"Arjun",'date_of_birth':'17/12/1970','favourite_colour':"Blue",'age':50}
for values in d:    #gathering values using dictionary[key]
    print("values :",d[values])
    print("values :",d.get(values))
for values in d.values():   #gathering values using values method 
    print("values :",values)
"""
#Removing keys and values from dictionary
"""
d={"Hero":"Arjun",'date_of_birth':'17/12/1970','favourite_colour':"Blue",'age':50}
d.pop("favourite_colour") #To remove specific key value pair from dictionary
print("After using pop method new dictionary :",d)
d.popitem()#To remove last key value pair from dictionary
print("After using popitem method new dictionary :",d)
d.clear()
print("Dictionary after clear :",d)
del d
print("Dictionary after deleting :",d)
"""
#Binding two different lists into dictionary
# l1=['Hero','age']
# l2=['Arjun',20]
# d=dict(l1,l2)
# print("dictionary :",d)

#For loop for items method
"""
d={"Hero":"Arjun",'date_of_birth':'17/12/1970','favourite_colour':"Blue",'age':50}
print("Items :",d.items())
for keys,values in d.items():
    # print("type of keys :",type(keys))
    # print("type of values :",type(values))
    print("keys :",keys,values)
    print("values :",values)

"""
#copying dictionary
"""
d={"Hero":"Arjun",'date_of_birth':'17/12/1970','favourite_colour':"Blue",'age':50}
d1=d.copy()     #Using copy method
print("New dictionary d1:",d1)
d2=d            #Using assignment operator
print("New dictionary d2:",d2)
d3=dict(d)      #Using dict constructor
print("New dictionary d3:",d3)
"""
#Nested dictionaries
"""
d={"Benz":{"Engine":"a1","cost":3000000,"colour":"blue"},"Ferrari":{"Engine":"a2","cost":5000000,"colour":"Green"}}
print("printing dictionary :",d)
print("printing Benz dictionary :",d["Benz"])
print("type Benz dictionary :",type(d["Benz"]))
print("printing Ferrari dictionary :",d["Ferrari"])
print("type Ferrari dictionary :",type(d["Ferrari"]))
print("printing Ferrari engine :",d["Ferrari"]['Engine'])
print("type of Ferrari engine :",type(d["Ferrari"]['Engine']))
"""
#Creating new dictionary with existing dictionaries
car={"Benz":{"Engine":"a1","cost":3000000,"colour":"blue"},"Ferrari":{"Engine":"a2","cost":5000000,"colour":"Green"}}
Animal={"Girafee":{"length":16,"colour":"orange"},"Lion":{"Food_habits":"Meat","lives_in":"forest"}}
world={
    "car":car,
    "Animal":Animal
}
print("World :",world)
print("cars :",world['car'])
print("gathering ferrari values from cars :",world['car']['Ferrari'])