# Exception Hadling

try:
	print(x)
except NameError:
	print("Variable x is not defined")
except:
	print("Someting else went wrong")
print("-------------------")

# Else

try:
	print("Hello")
except:
	print("Something went wrong")
else:
	print("Nothing went wrong")
print("-------------------")

# Finally

try:
	print(x)
except:
	print("Someting went wrong")
finally:
	print("The 'try except' is finished")
print("-------------------")

# Raise an exception

x = -1

if x < 0:
	raise Exception("Sorry, no numbers below zero")
print("-------------------")