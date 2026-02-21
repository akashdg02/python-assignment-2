def q20_math_menu():
    n = int(input("Enter N: "))
    # Armstrong Logic: sum of digits raised to power of count [cite: 204]
    digits = [int(d) for d in str(n)]
    is_arm = sum(d**len(digits) for d in digits) == n
    print(f"Armstrong: {is_arm}")