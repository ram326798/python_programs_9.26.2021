import json

"""
#json data
j='{"hero":"prabhas","villian":"rana","movie":"Bahubali"}'

# print("json data",j['hero'])  ##json data does'nt have key value pairs so it will throw error when i call key
#converting json into python object using loads() --result will be dictionary
p=json.loads(j)

print("python object",p['hero'])
"""

# converting python object into json data using dumps()
p = {"hero": "prabhas", "villian": "rana", "movie": "Bahubali"}
print(type(p))

# converting into json

j = json.dumps(p)

print(type(j))
print(j)

print("indentation :",json.dumps(p,indent=4)) #indentation in order to understand developers

print("indentation with sorting :",json.dumps(p,indent=4,sort_keys=True))
