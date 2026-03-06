# Question 1

# Create a list of 5 numbers and print all numbers using a loop.
# Example output
# 10
# 20
# 30
# 40
# 50

# Solution

# nums = [10,20,30,40,50]

# for i in nums:
#     print(i)


# Question 2

# Create a list of 5 fruits and print the first fruit.

# fruits = ['mango','banana',"Apple","Graps","Orange"]

# print(fruits[0])


# Question 3

# Write a program that adds a new number to a list using append().
# Example output
# [10, 20, 30, 40]

# Solution

# nums = [10,20,30]
# nums.append(40)

# print(nums)

# Small Task

# Student Marks List
# Create a list:
# marks = [70, 80, 90, 60, 85]
# Write a program to:

# Print all marks
# Print total marks
# Print average marks
# Solution

marks = [70, 80, 90, 60, 85]

print(marks)

total = 0
for i in marks:
    total = total + i
print("Total marks is: ",total)

avg = 0
avg = total/len(marks)

print("The avgerage marks is: ",avg)