# Task 1
# Create list comprehension that produces:
# [10,20,30,40]
# From:
# nums = [1,2,3,4]

# Solution 

# nums = [1,2,3,4]

# result = [n*10 for n in nums]

# print(result)



# Task 2
# Create dictionary where:
# numbers → squares
# Example:
# [2,3,4]
# Expected:
# {2:4, 3:9, 4:16}


# Solution

# nums = [2,3,4]

# result = {n: n**2 for n in nums}

# print(result)


# 🚀 Mini Project
# Word Frequency Counter
# Sentence:
# "python is easy and python is powerful"
# Program should output dictionary like:
# {
# 'python':2,
# 'is':2,
# 'easy':1,
# 'and':1,
# 'powerful':1
# }
# Hint:
# split()
# dictionary
# loop


# solution

from collections import Counter

sentance  = "python is easy and python is powerful"

result = Counter(sentance.split())

print(result)
