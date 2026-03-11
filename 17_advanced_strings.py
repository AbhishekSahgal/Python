# Advanced strings 

# name = input("Enter your name: ")

# print(name.casefold())


# sentence = "Python is very powerful"

# words = sentence.split()

# print(words)


# sentance2 = ' '.join(words)

# print(sentance2)


# text = "I am a java deverloper"

# print(text.replace("java","python"))

# name = "Abhishek Sahagl"
# age = 21

# print(f"My name is {name} and i am {age} old")


# Take input sentence and print number of words.
# Example:
# Input: Python is very powerful
# Output: 4
# Hint:
# split()
# len()

# sentance = input("Enter your sentance: ")

# words = sentance.split()

# print(len(words))


# Task 2
# Convert this sentence into uppercase words list.
# "python makes coding easy"
# Expected:
# ['PYTHON','MAKES','CODING','EASY']

# Solution 

# text = "python makes coding easy"

# words = text.upper().split()

# print(words)


# 🚀 Mini Project
# Username Cleaner
# User enters username:
# "   Abhay_123   "
# Program should:
# remove spaces
# convert to lowercase
# Expected output:
# abhay_123
# Hint:
# strip()
# lower()

# Solution 

username = input("Enter username: ")

clean = username.strip().lower()

print(clean)

