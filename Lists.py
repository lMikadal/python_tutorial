# List
# List items are ordered, changeable, and allow duplicate values

thisList = ["a", "b", "c", "a"] 

print(thisList)
print(len(thisList))
print(type(thisList))
print("-----------------------")

# multiple type

tList = ["abs", 1, True]

print(tList)
print("-----------------------")

# list() Constructor

test = list(("apple", "banana", "cherry", "kiwi", "melon"))

print(test)
print("-----------------------")

# Access Items use index

print(test[1])
print(test[-1])
print(test[2:4])
print("-----------------------")

# Check if Item Exits

thisList = ["a", "b", "c"]

if "a" in thisList:
    print("in List")
print("-----------------------")

# Change Item Value

thisList = ["a", "b", "c", "d", "e"]

thisList[1] = "z"
print(thisList)

thisList[2:4] = ["y", "x"]
print(thisList)

thisList[2:4] = ["y", "x", "g", "H"]
print(thisList)

thisList[2:7] = "y"
print(thisList)
print("-----------------------")

# Insert Items

thisList = ["a", "b", "c", "d", "e"]

thisList.insert(2, "apple")
print(thisList)
print("-----------------------")

# Append Items

thisList = ["a", "b", "c"]

thisList.append("z")
print(thisList)
print("-----------------------")

# Extend List

t1 = ["a", "b", "c"]
t2 = ["d", "e", "f"]

t1.extend(t2)
print(t1)
print("-----------------------")

# Remove Specified Item

thisList = ["a", "b", "c", "d", "e", "f"]

thisList.remove("a")
print(thisList)
thisList.pop()
print(thisList)
del thisList # mean del list can't print

thisList = ["a", "b", "c", "d", "e", "f"]

thisList.clear() # clear thisList can print
print(thisList)
print("-----------------------")

# Loop for

thisList = ["a", "b", "c", "d", "e", "f"]

for x in thisList:
    print(x)
    
for i in range(len(thisList)):
    print(thisList[i])
print("-----------------------")

# Loop While

thisList = ["a", "b", "c", "d", "e", "f"]

i = 0
while i < len(thisList):
    print(thisList[i])
    i += 1
print("-----------------------")
    
# Looping Using List Comprehension

thisList = ["a", "b", "c", "d", "e", "f"]

[print(x) for x in thisList]
print("-----------------------")

# List Comprehension
# newList = ['expression' for 'item' in 'iterable' if 'condition == True' else 'condition == False']

t = ["apple", "banana", "cherry", "kiwi", "mango"]

x = [x for x in t if "a" in x]
print(x)
print("-----------------------")

# Sort List Alphanumerically

this = [4, 10, 1, -1]

this.sort()
print(this)
print("-----------------------")

# Sort Descending

this = [4, 10, 1, -1]

this.sort(reverse = True)
print(this)
print("-----------------------")

# Customize Sort Function
def myfunc(n):
    return abs(n - 50)

thisList = [100, 50, 65, 82, 23]
thisList.sort(key = myfunc) # sort result
print(thisList)
print("-----------------------")

# Copy a List

thisList = ["abc", "def", "ghi"]

clist = thisList.copy()
print(clist)

clist = list(thisList)
thisList.append("x")
print(clist)
print("-----------------------")

# Join Two List

l1 = [1, 2, 3]
l2 = ["a", 'b', 'c']

l3 = l1 + l2
print(l3)

for x in l2:
    l1.append(x)
print(l1)

l1.extend(l2)
print(l1)
print("-----------------------")