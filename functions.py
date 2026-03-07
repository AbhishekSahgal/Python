# Q1

# Create a function that prints:
# Hello Python

# Solution 

# def greet():
#     print("Hello python")

# greet()
# greet()
# greet()


# Q2

# Create a function that takes a name and prints:
# Hello <name>

# Solution 

# name = input("Enter Your name: ")

# def greet():
#     print("Hello", name)

# greet()

# Q3

# Create a function that takes two numbers and prints their sum.

# Solution 

# num1 = int(input("Enter Your first number: "))
# num2 = int(input("Enter Your secound number: "))

# def add():
#     return num1+num2

# print(add())


# Q4

# Create a function that takes a number and prints square of the number.

# Solution

# num2 = int(input("Enter Your secound number: "))

# def sqrt():
#     return num2*num2

# print(sqrt())


# Q5

# Create a function that returns sum of two numbers.


# Q6

# Create a function that returns the largest of two numbers.

# Solution


# def largest():
#     num1 = int(input("Enter Your first number: "))
#     num2 = int(input("Enter Your secound number: "))

#     if num1 > num2:
#         print("Number one is greater")
#     else:
#         print("Number second in greater")
    
# largest()


# Q7

# Create a function that returns average of three numbers.

# def avg():
#     num1 = int(input("Enter Your first number: "))
#     num2 = int(input("Enter Your secound number: "))
#     num3 = int(input("Enter Your third number: "))

#     return num1+num2+num3/3

# print("The average of three numbers is: ", avg())

# Q8

# Create a function that checks if a number is:

# Even
# Odd

# Solution

# def iseven():
#     num = int(input("Enter Your number: "))

#     if num % 2 == 0:
#         print("The given number is even")
#     else:
#         print("The given number is odd")

# iseven()


# Q9

# Create a function that prints the multiplication table of a number.

# def table():
#     num = int(input("Enter Your number: "))

#     for i in range(11):
#         print(num, "*" ,i ,"=" , num*i)

# table()


# Mixed Practice (Functions + Lists)
# Q11

# Create a function that returns sum of numbers in a list.
# Example
# [10,20,30]
# Output
# 60

# Solution 

# nums = [10,20,30]

# def sum():
#     total = 0
#     for i in nums:
#         total = total + i
#     return total

# print(sum())


# Mixed Practice (Functions + Dictionaries)
# Q14

# Create a function that prints all keys and values of a dictionary.

# Solution 

details = {
    "math" : 80,
    "science" : 70,
    "english" : 85
}

def dic():
    for i in details:
        print(i, end=" : ")
        print(details[i])

dic()