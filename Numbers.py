# Numbers

'''
int
float
complex

'''

# Int

x = 123456789
y = -987654321

print(type(x))
print(type(y))
print("----------------------------")

# Float

x = 12.34
y = -43.21
z = 35e2

print(type(x))
print(type(y))
print(type(z))
print("----------------------------")

# Complex ("j" as the imaginary)

x = 3+5j
y = 8j
z = -4j

print(type(x))
print(type(y))
print(type(z))
print("----------------------------")

# Type Conversion

x = 1
y = 2.8

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
print("----------------------------")

# Random Number

import random

print("random number =", random.randrange(1, 10))
print("----------------------------")