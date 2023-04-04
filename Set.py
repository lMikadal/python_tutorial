# Set
# Set items are unordered, unchangeable, and do not allow duplicate values

# Duplicates Not Allowed

thisset = {"apple", "banana", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2} # True and 1 same value

print(thisset)
print(type(thisset))
print(len(thisset))
print("-----------------")

# Access Items

for x in thisset:
    print(x)
    
print("apple" in thisset)
print("-----------------")

# Add Items

thisset = {'a', 'b', 'c'}

thisset.add("apple")
print(thisset)

s2 = {1, 2, 3}

thisset.update(s2)
print(thisset)
print("-----------------")

# Remove Item

#thisset.remove('z') # if doesn't exist, display error
thisset.remove('a')
print(thisset)

thisset.discard('a') # if doesn't display error
print(thisset)

x = thisset.pop() # random remove
print(x)
print(thisset)

thisset.clear() # can print
print(thisset)

del thisset # can't print
print("-----------------")

# Loop Items

thisset = {'a', 'b', 'c', 'd'}

for x in thisset:
    print(x)
print("-----------------")

# Join Two Sets

s1 = {'a', 'b', 'c'}
s2 = {1, 2, 3}

s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)
print("-----------------")

# Keep ONLY the Duplicates

x = {"apple", "banana"}
y = {"orange", "apple"}

z = x.intersection(y)
print("x", x)
print("z", z)

x.intersection_update(y)
print(x)
print("-----------------")

# Keep All, But NOT the Duplicates

x = {"apple", "banana", "orange"}
y = {"google", "os", "apple"}

z = x.symmetric_difference(y)
print(z)

x.symmetric_difference_update(y)
print(x)
print("-----------------")