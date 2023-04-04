# Classes/Objects
#Create a Class

class MyClass:
    x = 5
    
# Create Object

p1 = MyClass()
print(p1.x)
print("---------------------")

# The __init__() Function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("Petch", 23)

print(p1.name)
print(p1.age)
print("---------------------")

# The __str__() Function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self): 
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)

print(p1)
print("---------------------")

# Modify Object Properties

p1.age = 40

print(p1.age)
print("---------------------")

# Delete Object Properties

del p1.age

print(p1.name)
# print(p1.age) # can't print because del
del p1

# print(p1) # can't print because del
print("---------------------")

# The pass Statement

class Person:
    pass
print("---------------------")