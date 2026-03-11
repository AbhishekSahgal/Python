# Task 1
# Remove duplicates from this list:
# nums = [5,5,6,7,7,8,9]
# Expected result:
# {5,6,7,8,9}


# Solution

# nums = [5,5,6,7,7,8,9]

# print(set(nums))



# Task 2
# Find common numbers between two lists.
# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# Expected output:
# {3,4}
# Hint:
# set(list1) & set(list2)

# Solution

# list1 = [1,2,3,4]
# list2 = [3,4,5,6]

# print(set(list1) & set(list2))


# 🚀 Mini Project
# Unique Word Finder
# Program:
# sentence = "python is fun and python is powerful"
# Goal:
# Print unique words.
# Hint:
# split()
# set()
# Expected idea:
# {'python','is','fun','and','powerful'}

# Solution

sentence = "python is fun and python is powerful"

words = sentence.split()

print(words)

print(set(words))