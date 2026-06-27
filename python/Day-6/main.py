# # What is a For Loop?

# # A for loop repeats code a specific number of times or goes through items one by one.

# # for example 
# # for i in range(6):
# #     print(i)
    
    
#     # For Loop Syntax
#     # for variable in sequence:
#     # # code
    
# # for example 
# # 
# # for number in range(1,6):
# #     print(number)
    
    
#     # Understanding range()
    
#     # 1.range(5)

# print("-----------1----------------")
# for num in range(5):
#     print(num)
    
#     # Starts at 0 and stops before 5.
    
#     # 2. range(1,6)

# print("-------------2--------------")

# for i in range(1,6):
#     print(i)
    
#     # Starts at 1 and stops before 6.
    
    
#     # 3.range(2,12,2)
# print("-----------3----------------")
# for number in range(2,12,2):
#     print(number)
    
#     # range(start, stop, step)
    
#     # Counting Down
    
# for count in range(10,0,-1):
#     print(count)
    
    # Loop Through a String
    
# name="moge"

# for letters in name:
#     print(letters)
    
    # Loop Through a List
    
# fruets=["apple","orange", "mango"]

# for fruit in fruets:
#     print(fruets)
    
    
    # Using break
    
    
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# # Using continue

# for i in range(1, 6):
#     if i == 3:
#         continue

#     print(i)


# Nested For Loops

# for col in range(3):
#     for row in range(3):
#         print("*", end="")
     
#     print()
    
    

