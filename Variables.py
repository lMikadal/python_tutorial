# Creating Variables
x = 5
y = "Test"

print(x)
print(y)
print("--------------------------------------")

# Casting
x = str(3)		# x will be '3'
y = int(3)		# y will be 3
z = float(3)	# x will be 3.0

print(x, type(x))
print(y, type(y))
print(z, type(z))
print("--------------------------------------")

# Single or Double Quotes
x = "Test x"
y = 'Test y'
#is the same as

# Case-Sensitive
a = 4
A = "TestA"

print(a)
print(A)
print("--------------------------------------")

# Variable Names
#   - start with a letter or the underscore character
#   - Can't start with a number
#   - Can use (A-z, 0-9, _)
#   - Can't use keywords in Python

# Many Valuse to Multiple Variables

x, y, z = "testX", "testY", "testZ"

print(x)
print(y)
print(z)
print("--------------------------------------")

# One Value to Multiple Variables

x = y = z = "testXYZ"
print(x)
print(y)
print(z)
print("--------------------------------------")

# Unpack a Collection

test = ["val1", "val2", "val3"]
x, y, z = test

print(x)
print(y)
print(z)
print("--------------------------------------")

# Output Variables

x = "Python"
y = "is"
z = "awesome"

print(x, y, z)
print(x + y + z)
print("--------------------------------------")

# Global Variables

x = "OutTestX"

def myfunc():
	x = "InTestX" # if x in func print("InTestX")
	print("Python print " + x)

myfunc()
print("Python print " + x)
print("--------------------------------------")

# The global Keyword

def myfunc():
	global x
	x = "TestGlobal"

myfunc() # must use func

print("Python print " + x)
print("--------------------------------------")