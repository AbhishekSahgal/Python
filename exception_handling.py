# Q1

# Write a program that handles division by zero.

# try:
#     num = int(input("Enter your number: "))
#     result = 10/num
# except ZeroDivisionError:
#     print("You cannot devide by zero")    


# Q2

# Ask user for a number and handle invalid input.

# Example:
# Enter number: abc
# Invalid input

# try:
#     num = int(input("Enter your number: "))
#     result = 10/num

# except ValueError:
#     print("You are not input string")


# Q4

# Create a list:
# [10,20,30]
# Ask user for index and handle IndexError.

# nums = [10,20,30]

# try:
#     forindex = int(input("Enter index that you want to print: "))
#     print(nums[forindex])
# except:
#     print("You are enter wrong index")



# Practice — File Handling + Exceptions
# Q5

# Open a file and handle FileNotFoundError.


# try:
#     with open("sahgal.txt", 'r') as file:
#         content = file.read()

# except FileNotFoundError:
#     print("File does not exist, before create this file then open")



# Q7

# Ask user to enter numbers until valid input is given.

# Use try–except inside a loop.


nums = [10, 20, 30]

while True:
    try:
        index = int(input("Enter index that you want to print: "))
        print(nums[index])
        break
    except:
        print("Invalid input! Try again.")

