# Task 1
# Create tuple:
# (5,10,15,20)
# Print all numbers using loop.

# Solution

# numbers = (5,10,15,20)

# for i in numbers:
#     print(i)


# Task 2
# Use tuple unpacking.
# Tuple:
# person = ("Abhay",25,"India")
# Print:
# name
# age
# country

# SOlution

# x,y,z = ("Abhishek Sahgal" , 21, "Lucknow")

# print(x)
# print(y)
# print(z)


# 🚀 Mini Project
# Coordinate Distance Calculator
# Store coordinates:
# point1 = (2,3)
# point2 = (5,7)
# Calculate distance using formula:
# √((x2-x1)^2 + (y2-y1)^2)
# Hint:
# math.sqrt()
# tuple unpacking

# Solution

import math as m

x,y = (2,3)
p,q = (5,7)

distance = m.sqrt(((p-x)**2) + (q-y)**2)

print(distance)