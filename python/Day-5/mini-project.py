# Mini Project 1: Number Guessing Game

secret=7
gues=0
 
while gues !=secret:
    gues=int(input("gues the number:"))
    
    if gues!=secret:
        print("try againg..")

print ("You won!")
    