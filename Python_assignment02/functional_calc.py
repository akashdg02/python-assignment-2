def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "ZeroDivError"

def q18_functional_calc():
    # Menu-driven main function [cite: 197]
    print("1. Add 2. Sub 3. Mult 4. Div")
    choice = input("Enter choice (1-4): ")