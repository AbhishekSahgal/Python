# Question 1

# Print this pattern:

# *
# **
# ***
# ****
# *****

# Solution

# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print("")


# Small Challenge for You
# Try printing this pattern:

# *****
# ****
# ***
# **
# *

# Solution 

# for i in range(6):
#     for j in range(5-i):
#         print("*",end="")
#     print()

# Small Challenge (Try Yourself)
# Print this pattern:

# 1
# 22
# 333
# 4444
# 55555

# for i in range(6):
#     for j in range(i):
#         print(i,end="")
#     print()


# Question 2

# Print numbers like this:

# 1
# 12
# 123
# 1234
# 12345

# Solution 

for i in range(6):
    for j in range(i):
        print(j+1,end="")
    print()