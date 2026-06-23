# # PART 1 — What a while loop actually does

# # here a comparison between if and while loop

# # Version 1 — if statement
# # spam=0

# # if spam<5:
# #     print("hello,world")
# #     spam=spam+1
    
#     # Version 2 — while loop
    
# # spam=0

# # while spam<5:
# #     print('hello,mohamed')
    
# #     spam+=1
    
    
#     # PART 2 — The danger: infinite loops
    
# # while True:
# #     print("hello,world")


# # PART 4 — break: escaping a loop early


# # while True:
# #     print('Please type your name.')
# #     name=input()
# #     if name=="your name":
# #         break
# # print("thank you")


# # while True:
# #     print("Logging")
    
# #     username=input("Ente username.")
# #     password=input("Passwor")
    
# #     if username =="moha4414" and password=="4414":
# #         break

# # print("Access guranted 😁" )


# # The networking connection — very real
# while True:
#     print('Enter device IP to check (or type exit to stop):')
    
#     ip=input()
    
#     if ip =="exit":
        
#         break
#     print('Checking ' + ip + '...')


# PART 5 — continue: skipping to the next round

