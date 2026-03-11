# Task 1
# Create list:
# numbers = [1,2,3,4,5]
# Using list comprehension create:
# [1,4,9,16,25]

# Solution

# numbers = [1,2,3,4,5]


# result = [n*n for n in numbers]
# print(result)


# Task 2
# From list:
# numbers = [10,15,20,25,30]
# Create list of numbers divisible by 10.
# Expected output:
# [10,20,30]

# Solution

# numbers = [10,15,20,25,30]

# output= [n for n in numbers if n % 10 == 0 ]

# print(output)


# 🚀 Mini Project
# Word Length Analyzer
# Input:
# words = ["python","developer","ai","code"]
# Create list containing length of each word.
# Expected output:
# [6,9,2,4]
# Hint:
# len()
# list comprehension


words = ["python","developer","ai","code"]

output = [len(n) for n in words]

print(output)


