# 🚀 Mini Project
# Student Marks Analyzer
# Program should:

# Store students like this:

# students = [
#     {"name":"Abhay","marks":90},
#     {"name":"Rahul","marks":70},
#     {"name":"Neha","marks":85}
# ]
# Program prints:

# Top student
# Average marks
# All student names

#  Solution


students = [
    {
        "name":"Abhay",
        "marks":90
     },
    {
        "name":"Rahul",
        "marks":70
    },
    {
    "name":"Neha",
    "marks":95
    }
]

top_student = students[0]

for student in students:
    if student['marks'] > top_student['marks']:
        top_student = student

print("Top student nme is: ",top_student['name'])

total = 0

for student in students:
    total = total + student['marks']

result = total/len(student)

print("Average is: ",result)

print("All students name is")

for student in students:
    print(student['name'])