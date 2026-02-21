def q2_simple_calc():
    try:
        # Ask user for two numbers [cite: 46]
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Display results for all operations [cite: 47]
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} * {num2} = {num1 * num2}")
        
        # Handle division by zero edge case [cite: 12]
        if num2 != 0:
            print(f"{num1} / {num2} = {round(num1 / num2, 2)}")
            print(f"{num1} % {num2} = {num1 % num2}")
        else:
            print("Division/Modulus: Error (Division by zero)")
            
        print(f"{num1} ^ {num2} = {num1 ** num2}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")