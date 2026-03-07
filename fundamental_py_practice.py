# Question 1

# Print this pattern:

# *
# **
# ***
# ****
# *****

# Solution

# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print("")


# Small Challenge for You
# Try printing this pattern:

# *****
# ****
# ***
# **
# *

# Solution 

# for i in range(6):
#     for j in range(5-i):
#         print("*",end="")
#     print()

# Small Challenge (Try Yourself)
# Print this pattern:

# 1
# 22
# 333
# 4444
# 55555

# for i in range(6):
#     for j in range(i):
#         print(i,end="")
#     print()


# Question 2

# Print numbers like this:

# 1
# 12
# 123
# 1234
# 12345

# Solution 

# for i in range(6):
#     for j in range(i):
#         print(j+1,end="")
#     print()

# Question 3

# Print reverse numbers:

# 5
# 54
# 543
# 5432
# 54321

# for i in range(6):
#     for j in range(5,5-i,-1):
#         print(j, end="")
#     print() 

# Type 2 — Counting Problems (Loops + Conditions)

# Question 4
# Count how many even numbers exist between 1 and 100.
# Expected output example:
# Total even numbers: 50

# Solutions


# count = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         count = count + 1
# print("Total even numbers is: ",count)

# Question 5

# Count how many numbers between 1 and 50 are divisible by 3.

# count = 0
# for i in range(1,51):
#     if i % 3 == 0:
#         count = count + 1
# print(count)

# Question 6

# Take a number from the user and count how many digits it has.

# Example:
# Enter number: 5678
# Total digits: 4

# Solution

# number = input("Enter number: ")

# count = len(number)
# print(count)

# Type 3 — List Logic

# Question 7

# Given this list:
# numbers = [5, 10, 15, 20, 25]

# Print only numbers greater than 15.

# Expected output:
# 20
# 25

# numbers = [5, 10, 15, 20, 25]

# for i in numbers:
#     if i > 15:
#         print(i)


# Question 8

# From a list of numbers, print only even numbers.

# Example list:
# [3, 6, 9, 12, 15, 18]
# Expected output:

# 6
# 12
# 18

# Solution

# numbers = [3, 6, 9, 12, 15, 18]

# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# Question 9

# Reverse a list using a loop.
# Example:

# Original list: [1,2,3,4]
# Reversed list: [4,3,2,1] 

# list = [1,2,3,4]

# for i in range(len(list)-1,-1,-1):
#     print(list[i])



# Type 4 — Dictionary Logic

# Question 10
# Create a dictionary storing student marks.
# Example:

# {
#  "math": 80,
#  "science": 70,
#  "english": 85
# }

# Find the subject with the highest marks.

# details = {
#     "math" : 80,
#     "science" : 70,
#     "english" : 85,
# }

# highest_marks = 0

# for i in details:
#     if details[i] > highest_marks:
#         highest_marks = details[i]

# print("highest marks: ", highest_marks)


# Print only the subjects where marks are greater than 75.


# details = {
#     "math" : 80,
#     "science" : 60,
#     "english" : 85,
# }

# max = {}

# for i in details:
#     if details[i] > 75:
#         max[i] = details[i]

# for j in max.keys():
#     print(j)


# Question 12

# Count how many subjects exist in the dictionary.

# Solution 

# details = {
#     "math" : 80,
#     "science" : 60,
#     "english" : 85,
# }

# count = 0

# for i in details.keys():
#     count = count + 1

# print(count)/


# Question 13

# Take 5 numbers from the user and store them in a list.

# Print:
# Largest number
# Smallest number

# Solution

# nums = []

# for i in range(5):
#     store = int(input("Enter five numbers: "))
#     nums.append(store)

# largest = nums[0]
# smallest = nums[0]

# for j in range(5):
#     if nums[j] > largest:
#         largest = nums[j]
#     if nums[j] < smallest:
#         smallest = nums[j]

# print(largest)
# print(smallest)


# Question 14

# Create a list and calculate:
# Total
# Average

# numbers = [10,20, 30, 15, 45]

# total = 0
# average = 0

# for i in numbers:
#     total = total + i

# average = total / len(numbers)

# print(total)
# print(average)

# Question 15

# Remove duplicate numbers from a list.
# Example:
# Input: [1,2,2,3,4,4,5]
# Output: [1,2,3,4,5]


