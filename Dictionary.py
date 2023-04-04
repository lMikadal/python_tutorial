# Dictionaries
# Dictionary items are ordered, changeable, and does not allow duplicates

thisdict = {
    "name": "petch",
    "aga": 23
}

print(thisdict["name"])
print("------------------------------------")

# Duplicates Not Allowed

thisdict = {
    "name": "petch",
    "age": 23,
    "year": 1999,
    "year": 2023,
    "colors": ["red", "white", "blue"]
}

print(thisdict)
print(len(thisdict))
print(type(thisdict))
print("------------------------------------")

# Constructor

thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict)
print("------------------------------------")

# Accessing Items

x = thisdict['name'] # same
print(x)
x = thisdict.get("name") # same
print(x)
print("------------------------------------")

# Get Keys

x = thisdict.keys()
print(x)

thisdict['colors'] = "white"
print(x) # key thisdict
print("------------------------------------")

# Get Values

x = thisdict.values()
print(x)

thisdict['colors'] = "red"
print(x) # values thisdict
print("------------------------------------")

# Get Items

x = thisdict.items()
print(x)

thisdict["year"] = 2023
print(x)
print("------------------------------------")

# Check if Key Exists

if "name" in thisdict:
    print("Yes, have key 'name'!!")
print("------------------------------------")

# Change Values

thisdict['name'] = "petch"
print(thisdict)

thisdict.update({'name': "panupong"})
print(thisdict)
print("------------------------------------")

# Adding Items

thisdict["study"] = "42bkk"
print(thisdict)

thisdict.update({"project": "miniRT"})
print(thisdict)
print("------------------------------------")

# Removing Items

thisdict.pop("study")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict['name']
print(thisdict)

thisdict.clear()
print(thisdict)

del thisdict # can't print
print("------------------------------------")

# Loop Through a Dictionary

thisdict = {
    "name": "petch",
    "age": 23,
    "year": 1999,
    "year": 2023,
    "colors": ["red", "white", "blue"]
}

for x in thisdict:
    print(x)
print("------------------------------------")
    
for x in thisdict:
    print(thisdict[x])
print("------------------------------------")

for x in thisdict.values():
    print(x)
print("------------------------------------")

for x in thisdict.keys():
    print(x)
print("------------------------------------")

for x, y in thisdict.items():
    print("key =", x, "value = ", y)
print("------------------------------------")

# Copy a Dictionary

cpdict = thisdict.copy()
print(cpdict)

cpdict = dict(thisdict)
print(cpdict)
print("------------------------------------")

# Nested Dictionaries

myfamily = {
    "c1" : {
    	"name" : "p",
    	"age"  : 23
	},
    "c2" : {
    	"name" : "t",
    	"age"  : 2
	},
}

print(myfamily)

print(myfamily["c2"]['name'])
print("------------------------------------")