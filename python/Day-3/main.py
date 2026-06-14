# # This is a comment — Python skips this line completely
# print('Hello')   # this comment is at the end of a line


# # part 2 print() function

# print("hello")
# print("ip adrress:192.168.1.1")

# # print () prints a blank line  

# # one importan rule print can store strings and integers seperetally but can not  mix them+unless you convert types first 

# print("avaible ports "+str(24))
# print("what is your name")
# # print("availible ports"+24)  This will show error because of mixing string and integers without converting them

# # print("avaible ports",24) This also works because comma seperates them


# # PART 3 — The input() function

# device=input()

# print("You entered:"+device)

# age=input()

# print(age)

# # PART 4 — The len() function

# device="switch"

# print(len(device))
# # print(len()) shows error
# ip_address="192.168.1.1"
# print(" the lenth of the ip address:",len(ip_address))

# ip = input()
# if len(ip) < 7 or len(ip) > 15:
#     print('That does not look like a valid IP')

# PART 5 — Type conversion: str(), int(), float()

print(str(24))
print(int("-99"))
print(float(43))

age='23'

print(int(age))

password=4414
print(str(password))

print(int(1.99))

age=input("Enter your age:")

print("You are "+str(int(age))+" years old")