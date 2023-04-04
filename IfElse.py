# If ... Else

a = 33
b = 44

if b > a:
	print("b is greater than a")
elif b == a:
	print("a and b are equal")
else:
	print("a is greater than b")
print("--------------------------")

# Short Hand if ... else
print("a is greater than b") if a > b else print("b is greater than a")
print("a is greater than b") if a > b else print("=") if a == b else print("b is greater than a")
print("--------------------------")

# And

c = 50

if b == a and c > a:
	print("Both conditions are True")
print("--------------------------")

# Or

if a > b or c > a:
	print("At least one of the conditions is True")
print("--------------------------")

# Not

if not a > b:
	print("a is NOT greater than b")
print("--------------------------")

# Nested If

x = 41

if x > 10:
	print("Above ten,")
	if x > 20:
		print("and also above 20!")
	else:
		print("but not above 20.")
print("--------------------------")

# Thee pass Statement
# if statements cannot be empty

if b > a:
	pass
print("--------------------------")