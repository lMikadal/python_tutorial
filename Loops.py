# While Loops

i = 1
while i < 6:
    print(i)
    i += 1
print("------------------------")

# The break Statement

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("------------------------")

# The else Statement

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("------------------------")

# For Loops

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana": continue
    print(x)
    
for x in fruits:
    if x == "banana": break
    print(x)
    
for x in fruits[0]:
	print(x)
print("------------------------")

# range() Function

for x in range(6):
    print(x)
    
for x in range(10, 20):
    print(x)
print("------------------------")

# Else in For Loop

for x in range(6):
	print(x)
else:
	print("Finally finished!")

# If break else NOT executed

for x in range(6):
    if x == 3: 
        break
    print(x)
else:
	print("Finally finished!")
print("------------------------")

# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
print("------------------------")

# pass Statement

for x in [0, 1, 2]:
    pass
print("------------------------")