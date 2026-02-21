import math
import random

# --- GLOBAL UTILITIES ---
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a whole number.")

# --- QUESTIONS 1-20 ---

def q1():
    print("\n" + "="*30 + "\nSTUDENT BIO CARD\n" + "="*30)
    data = {"Name": "John Doe", "Age": "20 years", "Course": "Python Programming", 
            "College": "ABC University", "Email": "john@example.com"}
    for k, v in data.items():
        print(f"{k: <8}: {v}")
    print("="*30)

def q2():
    a, b = get_float("Num 1: "), get_float("Num 2: ")
    print(f"Add: {a+b}, Sub: {a-b}, Mult: {a*b}")
    print(f"Div: {a/b if b!=0 else 'Error'}, Mod: {a%b if b!=0 else 'Error'}, Exp: {a**b}")

def q3():
    s = input("Enter sentence: ")
    words = s.split()
    print(f"Original: {s}\nChars (w/ space): {len(s)}\nChars (no space): {len(s.replace(' ',''))}")
    print(f"Words: {len(words)}\nUPPER: {s.upper()}\nLower: {s.lower()}\nTitle: {s.title()}")
    if words: print(f"First: {words[0]}\nLast: {words[-1]}")
    print(f"Reversed: {s[::-1]}")

def q4():
    year = get_int("Birth year: ")
    age = 2024 - year # Current year as per assignment context
    print(f"Age: {age}, Months: {age*12}, Days: {age*365}, Hours: {age*365*24}, Mins: {age*365*24*60}")
    print(f"Years until 100: {100-age}")

def q5():
    bill = get_float("Total bill: ")
    ppl = get_int("People: ")
    tax = bill * (get_float("Tax %: ") / 100)
    tip = bill * (get_float("Tip %: ") / 100)
    total = bill + tax + tip
    print(f"Subtotal: {bill}\nTax: {tax}\nTotal: {total}\nPer Person: {total/ppl if ppl>0 else total}")

def q6():
    marks = [get_float(f"Subject {i+1}: ") for i in range(5)]
    total = sum(marks)
    perc = total / 5
    passed = all(m >= 40 for m in marks)
    grade = "F"
    if perc >= 90: grade = "A+"
    elif perc >= 80: grade = "A"
    elif perc >= 70: grade = "B"
    elif perc >= 60: grade = "C"
    elif perc >= 50: grade = "D"
    print(f"Total: {total}/500, Perc: {perc}%, Grade: {grade}, Result: {'Pass' if passed else 'Fail'}")

def q7():
    print("1.C>F 2.F>C 3.C>K 4.K>C 5.F>K 6.K>F")
    c = input("Choice: ")
    v = get_float("Value: ")
    if c=='1': print((v*9/5)+32)
    elif c=='2': print((v-32)*5/9)
    elif c=='3': print(v+273.15)
    elif c=='4': print(v-273.15)
    elif c=='5': print((v-32)*5/9+273.15)
    elif c=='6': print((v-273.15)*9/5+32)

def q8():
    y = get_int("Year: ")
    is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    reason = "Divisible by 4 and (not 100 or 400)" if is_leap else "Does not meet leap rules"
    print(f"{y} Leap Year: {is_leap} ({reason})")

def q9():
    age = get_int("Age: ")
    day = input("Day: ").lower()
    base = 0
    if age < 3: base = 0
    elif 3 <= age <= 12: base = 150
    elif 13 <= age <= 59: base = 300
    else: base = 200
    disc = 0.20 if day in ['friday', 'saturday', 'sunday'] else 0
    final = base * (1 - disc)
    print(f"Base: ₹{base}, Discount: {disc*100}%, Total: ₹{final}")

def q10():
    bal = 10000
    while True:
        cmd = input("\n1.Bal 2.Dep 3.With 4.Exit: ")
        if cmd == '1': print(f"Bal: ₹{bal}")
        elif cmd == '2': bal += get_float("Amount: ")
        elif cmd == '3':
            amt = get_float("Amount: ")
            if bal - amt >= 500: bal -= amt
            else: print("Insufficient (Min ₹500)")
        elif cmd == '4': break

def q11():
    h = get_int("Height: ")
    print("Pattern 1:")
    for i in range(1, h+1):
        print(" ".join(str(j) for j in range(1, i+1)))

def q12():
    n, r = get_int("Num: "), get_int("Range: ")
    for i in range(1, r+1):
        print(f"{n} x {i} = {n*i}")

def q13():
    count = get_int("How many numbers? ")
    nums = [get_float(f"Num {i+1}: ") for i in range(count)]
    if nums:
        print(f"Sum: {sum(nums)}, Avg: {sum(nums)/len(nums)}, Max: {max(nums)}, Min: {min(nums)}")

def q14():
    n = get_int("Number: ")
    if n < 0: print("Negative numbers not allowed.")
    else:
        res, steps = 1, []
        for i in range(n, 0, -1):
            res *= i
            steps.append(str(i))
        print(f"{n}! = {' x '.join(steps)} = {res}" if n > 0 else "0! = 1")

def q15():
    def is_p(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True
    n = get_int("Check: ")
    print(f"Prime: {is_p(n)}")
    s, e = get_int("Start: "), get_int("End: ")
    print([x for x in range(s, e+1) if is_p(x)])

def q16():
    target, tries = random.randint(1, 100), 7
    while tries > 0:
        g = get_int(f"Guess (Tries left {tries}): ")
        if g == target:
            print("Winner!"); return
        print("Too High" if g > target else "Too Low")
        tries -= 1
    print(f"Lost! It was {target}")

def q17():
    val = input("Enter: ").lower()
    rev = val[::-1]
    print(f"Original: {val}\nReversed: {rev}\nResult: {'PALINDROME' if val == rev else 'NOT'}")

def q18():
    def calc():
        while True:
            print("\n1.Add 2.Sub 3.Mult 4.Div 5.Mod 6.Pow 7.Exit")
            ch = input("Choice: ")
            if ch == '7': break
            a, b = get_float("A: "), get_float("B: ")
            if ch=='1': print(a+b)
            elif ch=='4' and b==0: print("Div Zero Error")
            # ... add other operations similarly
    calc()

def q19():
    def analyze(text):
        vowels = "aeiouAEIOU"
        v_count = len([c for c in text if c in vowels])
        words = text.split()
        print(f"Words: {len(words)}, Vowels: {v_count}, Reversed: {text[::-1]}")
    analyze(input("Text: "))

def q20():
    def math_menu():
        n = get_int("Enter N: ")
        # Sample logic for Armstrong
        s_n = str(n)
        p = len(s_n)
        is_arm = sum(int(d)**p for d in s_n) == n
        print(f"Armstrong: {is_arm}")
    math_menu()

# --- MAIN RUNNER ---
if __name__ == "__main__":
    while True:
        choice = get_int("\nEnter Question # (1-20, 0 to Exit): ")
        if choice == 0: break
        func_map = {1:q1, 2:q2, 3:q3, 4:q4, 5:q5, 6:q6, 7:q7, 8:q8, 9:q9, 10:q10,
                    11:q11, 12:q12, 13:q13, 14:q14, 15:q15, 16:q16, 17:q17, 18:q18, 19:q19, 20:q20}
        if choice in func_map: func_map[choice]()
        else: print("Invalid Question.")