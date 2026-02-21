def q4_age_calculator():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = 2024 # Current reference year
        age = current_year - birth_year
        
        # Conversions [cite: 91, 92, 93, 94, 95]
        print(f"Current age: {age}")
        print(f"Age in months: {age * 12}")
        print(f"Age in days: {age * 365}")
        print(f"Age in hours: {age * 365 * 24}")
        print(f"Age in minutes: {age * 365 * 24 * 60}")
        print(f"Years until age 100: {100 - age}")
    except ValueError:
        print("Please enter a valid year as a number.")