# Mini Project Logic — Simple To-Do List

# Goal
# Create a program where a user can:
# Add tasks
# View tasks
# Exit the program

# Example tasks:
# Study Python
# Practice coding
# Build a project

# tasks = []

# task = input("Enter Your task: ")
# task2 = input("Enter Your task: ")
# task3 = input("Enter Your task: ")

# tasks.append(task)
# tasks.append(task2)
# tasks.append(task3)

# print(tasks)

# another method

tasks = []

while True:
    task = input("Enter your task (type stop to finish): ")

    if task == 'stop':
        break
    else:
        tasks.append(task)

print("Your tasks is: ")

for t in tasks:
    print(t)


