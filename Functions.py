# Functions

def my_function():
    print("Hello from a function")
    
my_function()
print("---------------------")

# Arguments

def my_function(fname):
    print(fname + " Refsnes")

my_function("petch")
print("---------------------")

# Arbitrary Arguments, *args

def my_function(*arg):
    print("The youngest child is " + arg[2])
    
my_function("t1", "t2", "t3")
print("---------------------")

# Keyword Arguments

def my_function(c1, c2, c3):
	print(c1, c2, c3)

my_function(c3 = "c3", c2 = "c2", c1 = "c1")
print("---------------------")

# Arbitrary Keyword Arguments, **kwargs

def my_function(**kwargs):
	print(kwargs["test"])
        
my_function(test = "No test", NoTest = "test")
print("---------------------")

# Default Parameter Value

def my_function(country = "Thai"):
	print("I am from " + country)

my_function()
my_function("test")
print("---------------------")

# Return Values

def my_function(x):
    return 5 * x

print(my_function(5))
print("---------------------")

# The pass Statement

def myfunction():
	pass
print("---------------------")