# Built-in Data Types

"""
Text Type:		str
Numeric Types:	int, float, complex
Swquence Types:	list, tuple, range
Mapping Type:	dict
Set Types:		set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:		NoneType

"""

# Getting te Data Type

a = "Hello"
b = 5
c = 5.5
d = 1j
e = ["a", "b", "c"]
f = ("a", "b", "c")
g = range(6)
h = {"name": "panupong", "age": 24}
i = {"a", "b", "c"}
j = frozenset({"a", "b", "c"})
k = True
l = b"hello"
m = bytearray(5)
n = memoryview(bytes(5))
o = None

print("a =", type(a))
print("b =", type(b))
print("c =", type(c))
print("d =", type(d))
print("e =", type(e))
print("f =", type(f))
print("g =", type(g))
print("h =", type(h))
print("i =", type(i))
print("j =", type(j))
print("k =", type(k))
print("l =", type(l))
print("m =", type(m))
print("n =", type(n))
print("o =", type(o))
print("------------------------")