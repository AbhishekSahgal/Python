# Password Login System
# Program behavior:
# Correct password = "python123"
# User can try until correct

cpassword = "python123"

while True:
    password = input(("Enter password: "))
    if cpassword == password:
        print("Password is correct")
        break
    else:
        print("Try again")

