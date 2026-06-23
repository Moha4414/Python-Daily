# Mini Project 2: Simple Calculator Menu

while True:
    print("\n1. add")
    print("2. Exit")
    
    choice=input("Choice:")
    
    if choice=='1':
        a=int(input("Firts number:"))
        b=int(input("Secound number:"))
        
        print("Answer:",a+b)
        
    elif choice=="2":
        break