def q8_leap_year():
    year = int(input("Enter a year: "))
    
    # Rule: divisible by 4 AND (NOT 100 OR divisible by 400) [cite: 157]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year. Reason: It follows the divisibility rules.")
    else:
        print(f"{year} is NOT a leap year. Reason: It does not meet divisibility criteria.")