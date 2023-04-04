# Lambda
# Syntax => lambda arg : expression

x = lambda a : a + 10

print(x(5))
print("----------------")

# Functions

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
print("----------------")