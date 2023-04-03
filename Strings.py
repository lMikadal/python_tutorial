# Strings

print('Hello') # same
print("Hello") # same
print("------------------------------")

# Asssign Strign to a Variable

a = "Helloa"

print(a)
print("------------------------------")

# Multiling Strings

x = """lorem
test
python"""
y = '''lorem
test
python'''

print(x)
print(y)
print("------------------------------")

# Strings are Arrays

a = "Hello, World!"

print(a[0])
print("------------------------------")

# Looping Through a String

test = "ForTestLoopPython"

for x in test:
	print(x)
print("------------------------------")

# string Length

a = "test Hello, World!"

print(len(a))
print("------------------------------")

# Check String

txt = "The best things in life are free!"

print("the" in txt)
print("are" in txt)
print("are" not in txt)
print("------------------------------")

# Slicing

txt = "Hello, World!"

print(txt[2:5]) # print position 2 to 4 (not included 5)
print(txt[:5])
print(txt[2:])
print(txt[-5:-2]) # strat 1
print("------------------------------")

# upper Case

a = "Hello, World!"

print(a.upper())
print("------------------------------")

# Lower Case

a = "HELLO, World!"

print(a.lower())
print("------------------------------")

# Remove Whitespace

a = "  Hello  "

print("|" + a + "|")
print("|" + a.strip() + "|")
print("------------------------------")

# Replace String

a = "Hello, World!"

print(a.replace("l", "T"))
print("------------------------------")

# Split String

a = "Hello World"

print(a.split(" "))
print(a.split(" ")[0])
print(a.split(" ")[1])
print("------------------------------")

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)
print("------------------------------")

# String Format

age = 23
tell = 170
txt = "My age {}, tell {}"

print(txt.format(age, tell))
print(f"{age}")

txtt = "test {1}, {0}"
print(txtt.format(age, tell))
print("------------------------------")

# Escape Characters

'''

\'		Single Quote
\\		Backslash
\n		New Line
\r		Carriage Return
\t		Tab
\b		Backspace
\f		Form Feed
\ooo	Octal value
\xhh	Hex value

'''