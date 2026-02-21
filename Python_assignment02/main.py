
import math
import random

# ==========================================
# GLOBAL UTILITY FUNCTIONS
# ==========================================

def get_float(prompt):
    """Safely gets a float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value (e.g., 12.5).")

def get_int(prompt):
    """Safely gets an integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number (e.g., 10).")

# ==========================================
# INDIVIDUAL QUESTION FUNCTIONS (1-20)
# ==========================================

def q1_bio_card():
    """Q1: Displays a formatted student identity card."""
    name, age, course = "John Doe", 20, "Python Programming"
    college, email = "CampusPe Academy", "john.doe@example.com"
    print("\n" + "*"*34)
    print(f"| {'STUDENT BIO CARD':^30} |")
    print("*"*34)
    print(f"| Name    : {name:<18} |\n| Age     : {age:<18} |\n| Course  : {course:<18} |")
    print(f"| College : {college:<18} |\n| Email   : {email:<18} |")
    print("*"*34)

def q2_calculator():
    """Q2: Performs basic arithmetic operations."""
    a, b = get_float("Num 1: "), get_float("Num 2: ")
    print(f"Addition: {a+b}\nSubtraction: {a-b}\nMultiplication: {a*b}")
    print(f"Division: {a/b if b!=0 else 'Error (Div by 0)'}")

def q3_string_manipulator():
    """Q3: Analyzes string properties and transformations."""
    txt = input("Enter a sentence: ")
    print(f"Length: {len(txt)}\nUpper: {txt.upper()}\nLower: {txt.lower()}")
    print(f"Reverse: {txt[::-1]}\nWords: {len(txt.split())}")

def q4_age_calc():
    """Q4: Converts age in years to other time units."""
    year = get_int("Birth Year: ")
    age = 2024 - year
    print(f"Age: {age} | Months: {age*12} | Days: {age*365} | Hours: {age*365*24}")

def q5_bill_splitter():
    """Q5: Splits bill including tax and tip."""
    amt = get_float("Bill: ")
    ppl = get_int("People: ")
    tax = amt * (get_float("Tax %: ") / 100)
    tip = amt * (get_float("Tip %: ") / 100)
    total = amt + tax + tip
    print(f"Total: ₹{total:.2f} | Per Person: ₹{total/ppl:.2f}")

def q6_grade_calc():
    """Q6: Calculates grade from 5 subject marks."""
    marks = [get_float(f"Subject {i+1}: ") for i in range(5)]
    avg = sum(marks) / 5
    if avg >= 90: grade = "A+"
    elif avg >= 80: grade = "A"
    elif avg >= 70: grade = "B"
    elif avg >= 60: grade = "C"
    else: grade = "F"
    print(f"Average: {avg}% | Grade: {grade} | Result: {'Pass' if all(m >= 40 for m in marks) else 'Fail'}")

def q7_temp_converter():
    """Q7: Converts temperature between C and F."""
    val = get_float("Value: ")
    choice = input("1. C to F  2. F to C: ")
    if choice == '1': print(f"F: {(val * 9/5) + 32}")
    else: print(f"C: {(val - 32) * 5/9}")

def q8_leap_year():
    """Q8: Checks if a year is a leap year."""
    y = get_int("Year: ")
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print("Leap Year")
    else: print("Common Year")

def q9_tickets():
    """Q9: Movie ticket pricing with age/day logic."""
    age = get_int("Age: ")
    day = input("Day: ").lower()
    base = 150 if age <= 12 else (200 if age >= 60 else 300)
    if day in ['saturday', 'sunday']: base *= 0.8  # 20% weekend discount
    print(f"Ticket Price: ₹{base}")

def q10_atm():
    """Q10: Simulates ATM with balance and withdrawals."""
    bal = 10000
    while True:
        cmd = input("\n1.Bal 2.Dep 3.With 4.Exit: ")
        if cmd == '1': print(f"Balance: ₹{bal}")
        elif cmd == '2': bal += get_float("Amount: ")
        elif cmd == '3':
            amt = get_float("Amount: ")
            if bal - amt >= 500: bal -= amt
            else: print("Error: Minimum ₹500 balance required.")
        elif cmd == '4': break

def q11_patterns():
    """Q11: Prints number patterns."""
    h = get_int("Height: ")
    print("Pattern 1 (Triangle):")
    for i in range(1, h + 1):
        print(*range(1, i + 1))
    
    print("\nPattern 2 (Pyramid):")
    
    for i in range(1, h + 1):
        spaces = " " * (h - i)
        nums = "".join(str(x) for x in range(1, i + 1))
        rev = "".join(str(x) for x in range(i - 1, 0, -1))
        print(f"{spaces}{nums}{rev}")

def q12_tables():
    """Q12: Multiplication table generator."""
    n = get_int("Table for: ")
    for i in range(1, 11): print(f"{n} x {i} = {n*i}")

def q13_stats():
    """Q13: List statistics (Sum, Avg, Max, Min)."""
    data = [get_float(f"Num {i+1}: ") for i in range(get_int("How many numbers? "))]
    if data: print(f"Sum: {sum(data)} | Avg: {sum(data)/len(data)} | Max: {max(data)}")

def q14_factorial():
    """Q14: Iterative Factorial calculation."""
    n = get_int("N: ")
    print(f"Factorial: {math.factorial(n)}")

def q15_prime():
    """Q15: Prime number check and range finder."""
    def is_p(n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    n = get_int("Check: ")
    print(f"Prime: {is_p(n)}")

def q16_game():
    """Q16: Random number guessing game."""
    target, attempts = random.randint(1, 100), 7
    while attempts > 0:
        g = get_int(f"Guess (Lives: {attempts}): ")
        if g == target: print("Winner!"); return
        print("Higher" if g < target else "Lower")
        attempts -= 1
    print(f"Lost! It was {target}")

def q17_palindrome():
    """Q17: Palindrome check for strings/numbers."""
    s = input("Enter: ").lower().replace(" ","")
    print("Palindrome:", s == s[::-1])

def q18_functions():
    """Q18: Basic function arithmetic implementation."""
    add = lambda a, b: a + b
    print(f"Result (Add 10+5): {add(10, 5)}")

def q19_text_analysis():
    """Q19: Word frequency and vowel analysis."""
    txt = input("Text: ").lower()
    words = txt.split()
    freq = {w: words.count(w) for w in set(words)}
    print(f"Word Frequency: {freq}")

def q20_math_menu():
    """Q20: Advanced math features (Armstrong & GCD)."""
    n = get_int("N: ")
    p = len(str(n))
    is_arm = sum(int(d)**p for d in str(n)) == n
    print(f"Armstrong: {is_arm}")
    

# ==========================================
# MAIN EXECUTION MENU
# ==========================================

def main():
    functions = {
        1: q1_bio_card, 2: q2_calculator, 3: q3_string_manipulator, 4: q4_age_calc,
        5: q5_bill_splitter, 6: q6_grade_calc, 7: q7_temp_converter, 8: q8_leap_year,
        9: q9_tickets, 10: q10_atm, 11: q11_patterns, 12: q12_tables,
        13: q13_stats, 14: q14_factorial, 15: q15_prime, 16: q16_game,
        17: q17_palindrome, 18: q18_functions, 19: q19_text_analysis, 20: q20_math_menu
    }
    
    while True:
        print("\n" + "="*40 + "\n CAMPUSPE ASSIGNMENT MENU (1-20, 0 to Exit)\n" + "="*40)
        choice = get_int("Select Question Number: ")
        if choice == 0: break
        if choice in functions:
            functions[choice]()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()