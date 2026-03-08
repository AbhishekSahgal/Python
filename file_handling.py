# file = open("data.txt", "r")

# content = file.read()

# print(content)
# file.close


#  Reading Line by Line

# with open("data.txt", "r") as file:
#     for line in file:
#         print(line)


# 4️⃣ Reading Line by Line

# with open('data.txt', 'w') as file:
#     file.write(" Hello Abhishek sahgal, What are you doing curretly") 
#     file.write("\n Hello Abhishek sahgal,") 

# import os

# if os.path.exists("datamodel.txt"):
#     print("file exists")
# else:
#     print("File does not exist")



# Create a program that writes:
# Hello Python
# into a file named hello.txt.

# Solution

# with open("hello.txt", 'w') as file:
#     file.write("Hello Python")

# Q2

# Write a program that reads and prints the contents of hello.txt.

# Solution 

# with open("hello.txt", 'r') as file:
#     content = file.read()

# print(content)


# Q3

# Append this line to the file:
# Learning Python is fun

# Solution 

# with open("hello.txt", 'a') as file:
#     file.write(" Learning Python is fun")


# Q4

# Create a program that writes 5 numbers into a file.

# Example:

# 10
# 20
# 30
# 40
# 50

# with open("hello.txt", 'w') as file:
#     for i in range(1,6):
#         file.write(str(10*i) + "\n")
        

# Q6
# Read a file and print each line using a loop.

# with open("hello.txt", 'r') as file:
#     for i in file:
#         print(i.split())


# Q7

# Store this list into a file:

# ["Apple", "Banana", "Mango"]

# Each item should be written on a new line.

# Solution 

# list = ["Apple", "Banana", "Mango"]

# with open("hello.txt", 'w') as file:
#     for i in list:
#         file.write(i + "\n")


# Practice — Counting Lines
# Q8

# Write a program that counts how many lines exist in a file.

count = 0

with open("hello.txt", 'r') as file:
    for i in file:
        count = count + 1
        file.read()

