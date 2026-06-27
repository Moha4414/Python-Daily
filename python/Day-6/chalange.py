# Challenge for you

# Write a for loop that prints:

#     *****
#     *****
#     *****
#     *****
#     *****


# for row in range(5):
#     for col in range(5):
#         print("*",end="")
#     print()
    
    
    
#     Challenge 2

# Can you print this?

# *
# **
# ***
# ****
# *****

# for row in range(1,6):
#     for col in range(row):
#         print("*", end="")
        
#     print("")

# for row in range(6,0,-1):
#     for col in range(row):
#         print("*", end="")
    
#     print()


for row in range(1, 6):
    for col in range(row):
        print( ""," *",end="" )

    print()