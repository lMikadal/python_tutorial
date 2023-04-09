# Dates

import datetime

x = datetime.datetime.now()

print(x)
print("--------------")

# Date Output

print(x.year)
print(x.strftime("%A"))
print("--------------")

# Creating Date Objects

t = datetime.datetime(2020, 5, 17)

print(t)
print("--------------")

# The strftime() Method

print(t.strftime("%B"))
print("--------------")