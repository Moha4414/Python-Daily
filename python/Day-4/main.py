# # PART 2 — Boolean values: The foundation of all decisions

# True    # yes, correct, on
# False   # no, wrong, off



# # PART 3 — Comparison operators: How Python evaluates True or False


# # >>> 42 == 42        # equal to
# # True
# # >>> 42 == 99        # equal to
# # False
# # >>> 42 != 99        # not equal to
# # True
# # >>> 42 < 99         # less than
# # True
# # >>> 42 > 99         # greater than
# # False
# # >>> 42 <= 42        # less than OR equal to
# # True
# # >>> 42 >= 99        # greater than OR equal to
# # False

#      # assignment — puts a value INTO a variable =
#  # comparison — CHECKS if two values are equal ==
 
 
# #  example

# # ip = '192.168.1.1'        # = means STORE this value
# # ip == '192.168.1.1'       # == means IS this value equal to?

# # PART 4 — Boolean operators: Combining conditions

# # and    # both must be True
# # or     # at least one must be True
# # not    # flips True to False and False to True

# # print(True and True)

# # print(False and True)

# # print(True or False)

# # print(False or True)

# # print (not True)
# # print (not False)

# ip_reachable=True
# open_port=False


# #  both conditions must be true
# if ip_reachable and open_port:
#     print("Device is fully accessible")
    
#     # # OR — either condition is enough
    
# if ip_reachable or open_port:
#     print("Device is partially accessible")
    
#     # NOT — flip the result
    
# if not ip_reachable:
#     print("Device is unreachable")
    
    


# PART 6 — Nested if statements

print("Is device is reachable (yes/no)")

reachable=input()

if reachable=='yes':
    print("Device is reachable")
    print("Check SSH port (yes/no):")
    
    SSH=input()
    
    if SSH=='yes':
        print("SSH is open device fully accessible")
        
    else:
        print("SSH is closed-check firewall")

else:
    print("Device unreachable-check physical connection")

