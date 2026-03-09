# Q1

# Write a program that handles division by zero.

try:
    num = input("Enter your number: ")
    result = 10/num
except ZeroDivisionError:
    print("You cannot devide by zero")    