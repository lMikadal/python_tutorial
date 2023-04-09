# Use a Module

"""
import mymoudle

mymoudle.greeting("Petch")
print("--------------------")

test = mymoudle.person["name"]
print(test)
print("--------------------")
"""

# Re-naimg a Module

"""
import mymoudle as mx

mx.greeting("Petch")
print("--------------------")

test = mx.person["name"]
print(test)
print("--------------------")
"""

# Built-in Modules

import platform

x = platform.system()
print(x)
print("--------------------")

s = dir(platform)
print(s)
print("--------------------")

# Import From Module

from mymoudle import person

print(person["age"])
# print(mymoudle.greeting("Petch")) # Error
print("--------------------")