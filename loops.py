# Question 1

# Write a program to print numbers 1 to 20 using a loop.

# Solution
# for i in range(1,21):
#     print(i)

# Question 2

# Write a program to print even numbers from 1 to 50.

# Example output

# 2
# 4
# 6
# 8
# ...
# 50

# Solution

# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)

# Question 3

# Write a program that prints the multiplication table of a number.
# Example
# Enter number: 3
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30

# Solution

# num = int(input("Enter number: "))

# for i in range(1,11):
#     print(num, "*" , i ,"= " ,num*i)

# Small Task
# Sum of Numbers
# Write a program to calculate sum from 1 to 100.

# Expected output
# Sum is 5050

# Solution

# total = 0
# for i in range(1,101):
#     total = total+i
# print("Sum is ", total)

# Another method 
# print("Sum is: ",sum(range(1,101)))

# 1 se 100 ke even numbers ka sum nikale
# Example output:
# Sum of even numbers: 2550

total = 0

for i in range(1,101):
    if i % 2 == 0:
        total = total + i
print("Sum of even number is: ", total)
