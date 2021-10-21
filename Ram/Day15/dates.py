#in order to work with dates datetime need to import.

import datetime
"""
x = datetime.datetime.now()
print("current date :",x)
print("year:",x.year)   #In order to get year from current date

print(x.strftime("Week name:","%A")) #In order to get the day complete name
"""
#working with different dates
"""
d=datetime.datetime(1947,8,15) 
print("Independence day :",d)
print("Independence day year:",d.year)
print("Independence day year:",d.strftime("%Y"))
print("day name with three characters :",d.strftime("%a")) 
print("day complete name",d.strftime("%A")) #In order to get the day complete name
print("Month complete name :",d.strftime("%B"))
print("Month complete name :",d.strftime("%d"))
"""
#Working with specific format
d = datetime.datetime.now()
current_date=d.strftime("%Y/%m/%d")
print("current date :",current_date)