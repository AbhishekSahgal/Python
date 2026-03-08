# Mini Project — Calculator Using Functions

# Create functions:

# add()
# subtract()
# multiply()
# divide()

# Program menu:

# 1 Add
# 2 Subtract
# 3 Multiply
# 4 Divide

# Each option should call a separate function.


def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def mul(a,b):
    return a*b

def dev(a,b):
    return a/b

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your Second number: "))

print("1 for Addition")
print("2 for substraction")
print("3 for multiplication")
print("4 for division")


choice = int(input("Enter Your choice: "))



if choice == 1:
    print(add(num1,num2))
elif choice == 2:
    print(sub(num1,num2))
elif choice == 3:
    print(mul(num1,num2))
elif choice == 4:
    print(dev(num1,num2))
else:
    print("Wrong choice")
