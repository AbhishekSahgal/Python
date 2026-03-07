# Question 1

# Create a dictionary storing:
# name
# city
# age
# Print the city.

# solution 

# student = {
#     'name' : "Abhishek Sahgal",
#     'city' : "Lucknow",
#     'age': 21,
# }

# print("City name is: ", student['city'])


# Question 2

# Update the age in the dictionary.
# Example:
# age → 22
# Update to:
# age → 23

# Solution

# student = {
#     'name' : "Abhishek Sahgal",
#     'city' : "Lucknow",
#     'age': 21,
# }

# student['age'] = 23

# print("your updated age is: ",student['age'])


# Question 3

# Print all keys and values using a loop.
# Expected output example:
# name : Abhishek
# city : Kanpur
# age : 22

# Solution

# student = {
#     'name' : "Abhishek Sahgal",
#     'city' : "Lucknow",
#     'age': 21,
# }

# for i in student:
#     print(i, ":" , student[i])


# Small Task

# Create a dictionary about yourself.
# Store:
# name
# college
# course
# skills

# Then print something like:
# My name is ___
# I study at ___
# My skills are ___

name = input("Enter your name: ")
college = input("Enter your college: ")
cource = input("Enter your cource: ")
skills = input("Enter your skills: ")


mydetails = {
    'name' : name,
    'college' : college,
    'cource' : cource,
    'skills' : skills
}

print("My name is",mydetails['name'])
print("I study at",mydetails['college'])
print("My Skills are",mydetails['skills'])

