# Practice Questions — Modules

# Q1
# Import the math module and print:
# square root of 64

# Solution 

# import math as m

# print(m.sqrt(64))


# Q2
# Use the math module to print:
# factorial of 6

# Solution

# import math as m

# print(m.factorial(100))


# Q3
# Use the random module to generate a random number between 1 and 50.

# solution

# import random as r

# print(r.randint(1,50))


# Q4
# Create a list of fruits and randomly select one fruit.
# Example list:
# ["apple","banana","mango","orange"]

# Solution

# import random as r

# fruits = ["apple","banana","mango","orange"] 

# result = r.choice(fruits)

# print(result)


# Q5
# Print the current date

# Solution

# import datetime as d

# print(d.date.today())


# Q6
# Create a module called:
# my_math.py
# Add functions:
# add
# subtract
# Then import it in another program.

# Solution

import my_math as m

print(m.add(10,50))

