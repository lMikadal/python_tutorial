# Arithmetic operators

x, y = 5, 6

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
print("--------------------------")

# Assignment Operators

"""

x = 5 # print(5)
x += 3 # print(x + 3)
x -= 3 # print(x - 3)
x *= 3 # print(x * 3)
x /= 3 # print(x / 3)
x %= 3 # print(x % 3)
x //= 3 # print(x // 3)
x **= 3 # print(x ** 3)
x &= 3 # print(x & 3)
x |= 3 # print(x | 3)
x ^= 3 # print(x ^ 3)
x >>= 3 # print(x >> 3)
x <<= 3 # print(x << 3)

"""

# Comparison Operators

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print("--------------------------")

# Logical Operators

print(x < 5 and y < 10)
print(x < 5 or y < 10)
print(not(x < 5 and y < 10))
print("--------------------------")

# Identity Operators
# for compare the objectts

print(x is y)
print(x is not y)
print("--------------------------")

# Membership Operators

z = (5, 6, 7)

print(x in z)
print(x not in z)
print("--------------------------")

# Bitwise Operators

"""

&  => x & y		# bit same 1
|  => x | y		# bit or 1
^  => x ^ y		# bit some one 1
~  => ~x		# inverts all bit 0 to 1, 1 to 0
<< => x << 2	# left 2
>> => x >> 2	# right 2

"""

# Precedence

"""

()
**
+ - ~
* / // %
+ -
<< >>
&
^
|
== != > >= < <= is (is not) in (not in)
not
and
or

"""