
# # for loop

# print ("my name ")

# for i in range (5):
#     print("Mooge Five times ("+str(i)+")")
    
# total=0

# for num in range(101):
#    total=total+num
   
#    print(total)

# Check ports 1 through 1024 (common service ports)

# for port in range(1, 1025):
#     print("Checking port"+str(port))
    
  
    
    
    # Step through the last number of an IP range
# for last_oct in range(1,255):
#     ip="192.168.1."+str(last_oct)
#     print("scanning"+ip)

# import method 1 rondom
# import random

# for i in range(5):
    # print(random.randint(1,10))


# from random import *

# for i in range(3):
#     print(randint(1,10))


# # import sys

# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         # sys.exit()
#         print('You typed ' + response + '.')
    


# import sys 


# while True:
#     print("Enter your pasword")
    
#     password=int(input())
    
#     if password==1234:
#         sys.exit()
        
#         print("you typed "+password+".")


import sys

print('Enter command (or "quit" to stop the tool):')
command = input()

if command == 'quit':
    print('Shutting down network tool...')
    sys.exit()
    
    
    


