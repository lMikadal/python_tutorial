# Tuple
# Tuple items are ordered, unchangeable, and allow duplicate values

thistuple = ("apple", "banana", "cherry", "apple", "cherry")

print(thistuple)
print(len(thistuple))
print("------------------")

# Create Tuple With One Item

t = ("a",)
print(type(t))

t = ("a") # NOT Tuple
print(type(t))
print("------------------")

# Multiple Type

t1 = (1, "a", True)

print(t1)
print("------------------")

# Constructor

thistuple = tuple(("a", "b", "c"))

print(type(thistuple))
print(thistuple)
print("------------------")

# Access Tuple Items

thistuple = ("apple", "banana", "cherry", "apple", "cherry")

print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:4])
print(thistuple[:4])
print(thistuple[2:])
print("------------------")

# Check if Item Exists

if "apple" in thistuple:
    print("In Tuple")
print("------------------")
    
# Change Tuple Values

t = ('a', 'b', 'c')
l = list(t)
l[1] = 'z'
t = tuple(l)

print(t)
print("------------------")

# Add Items

t = ('a', 'b', 'c')
l = list(t)
l.append('z')
t = tuple(l)

print(t)

t1 = ('x',)
t += t1
print(t)
print("------------------")

# Remove Items

t = ('a', 'b', 'c')
l = list(t)
l.remove('a')
t = tuple(l)

print(t)

del t
#print(t) # Error
print("------------------")

# Unpacking a Tuple

fruits = ('apple', 'banana', 'cherry')
green, yellow, red = fruits

print(green)
print(yellow)
print(red)
print("------------------")

# Unpacking Asterisks*

fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
# green, yellow, *red = fruits
green, *yellow, red = fruits

print(green)
print(yellow)
print(red)
print("------------------")

# Loop Through a Tuple

fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
for x in fruits:
    print(x)
    
for i in range(len(fruits)):
    print(fruits[i])
    
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
print("------------------")

# Join Two Tuples

t1 = ('a', 'b', 'c')
t2 = (1, 2, 3)

t3 = t1 + t2
print(t3)
print("------------------")

# Multiply Tuples

t = ('a', 'b', 'c')
test = t * 2

print(test)
print("------------------")