def q11_patterns():
    h = int(input("Enter height: "))
    choice = input("Choose Pattern (1-4): ")
    
    if choice == '1': # Standard increment
        for i in range(1, h + 1):
            print(*range(1, i + 1))
    elif choice == '4': # Pyramid (Medium Difficulty) [cite: 169]
        for i in range(1, h + 1):
            print(" " * (h - i) + "".join(str(x) for x in range(1, i + 1)) + "".join(str(x) for x in range(i - 1, 0, -1)))