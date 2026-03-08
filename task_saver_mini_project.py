# Mini Project — Task Saver

# Create a program that:

# 1️⃣ asks user to enter tasks
# 2️⃣ stores tasks in tasks.txt
# 3️⃣ reads and displays saved tasks

# Concepts used:

# functions
# loops
# lists
# file handling

# Solution 

tasks = []
# function to add tasks

def add_tasks():
    while True:
        task = input("Enter Your task (type 'stop' to finish): ")

        if task.lower() == 'stop':
            break

        tasks.append(task)

# Fuction to save tasks to file

def save_tasks():
    with open('tasks.txt', 'a') as file:
        for task in tasks:
            file.write(task + "\n")


# function to read tasks from file

def show_tasks():
    print("saved tasks: ")

    with open("tasks.txt", 'r') as file:
        for line in file:
            print(line.split())

# program flow 

add_tasks()
save_tasks()
show_tasks()



