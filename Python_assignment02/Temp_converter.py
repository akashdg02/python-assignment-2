def q7_temp_converter():
    print("1. C to F  2. F to C  3. C to K  4. K to C  5. F to K  6. K to F")
    choice = input("Enter choice: ")
    temp = float(input("Enter temperature: "))
    
    # Logic using provided formulas [cite: 147, 149, 150, 151, 152, 153]
    if choice == '1': print(f"Result: {(temp * 9/5) + 32} F")
    elif choice == '2': print(f"Result: {(temp - 32) * 5/9} C")
    elif choice == '3': print(f"Result: {temp + 273.15} K")
    elif choice == '4': print(f"Result: {temp - 273.15} C")
    elif choice == '5': print(f"Result: {(temp - 32) * 5/9 + 273.15} K")
    elif choice == '6': print(f"Result: {(temp - 273.15) * 9/5 + 32} F")