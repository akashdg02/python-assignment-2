def q14_factorial():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Negative numbers not allowed.")
    else:
        res, steps = 1, []
        for i in range(n, 0, -1):
            res *= i
            steps.append(str(i))
        # Display step-by-step logic [cite: 182]
        print(f"{n}! = {' x '.join(steps)} = {res}" if n > 0 else "0! = 1")