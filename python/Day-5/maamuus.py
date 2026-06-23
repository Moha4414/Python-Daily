while True:
    print("\n--- MAAMUUS ---")
    print("1. Data")
    print("2. Ku Hadal")
    print("3. Data iyo Ku Hadal")
    print("4. Exit")

    choice = input("Dooro: ")

    if choice == "1":
        print("\n--- DATA ---")
        print("1. $0.15 = Internet aan xadidnayn, 3 saac")
        print("2. $0.05 = Internet aan xadidnayn, 20 daqiiqo")
        print("3. $0.25 = Internet aan xadidnayn, 8 saac")

    elif choice == "2":
        print("\n--- KU HADAL ---")
        print("1. $0.25 = Ku hadal aan xadidnayn, 15 saac")
        print("2. $0.05 = Ku hadal aan xadidnayn, 1 saac")
        print("3. $0.15 = Ku hadal aan xadidnayn, 6 saac")

    elif choice == "3":
        print("\n--- DATA IYO KU HADAL ---")
        print("1. $0.6 = Internet iyo ku hadal aan xadidnayn, 24 saac")
        print("2. $18 = Internet iyo ku hadal aan xadidnayn, 30 maalin")
        print("3. $0.5 = Internet iyo ku hadal aan xadidnayn, 20 saac")

    elif choice == "4":
        print("Nabad gelyo!")
        break

else:
    print("Doorasho khaldan!")z