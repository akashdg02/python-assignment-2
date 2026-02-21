def q20_math_menu():
    """
    Q20: Comprehensive Mathematical Number System.
    Includes advanced algorithms for number properties.
    """
    import math

    def get_fibonacci(n):
        """Returns the nth Fibonacci number."""
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def is_armstrong(n):
        """Checks if sum of digits raised to power of count equals n."""
        digits = [int(d) for d in str(n)]
        power = len(digits)
        return sum(d**power for d in digits) == n

    def get_gcd(a, b):
        """Euclidean Algorithm to find Greatest Common Divisor."""
        while b:
            a, b = b, a % b
        return a

    def is_perfect(n):
        """Checks if sum of proper divisors equals the number."""
        if n < 1: return False
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n

    # --- Menu Interface ---
    print("\n--- ADVANCED MATH MENU ---")
    print("1. Fibonacci  2. Armstrong Check  3. GCD & LCM  4. Perfect Number")
    choice = input("Select an option: ")
    num = int(input("Enter primary number: "))

    if choice == '1':
        print(f"The {num}th Fibonacci number is: {get_fibonacci(num)}")
    elif choice == '2':
        print(f"Is {num} an Armstrong number? {is_armstrong(num)}")
    elif choice == '3':
        num2 = int(input("Enter second number: "))
        gcd_val = get_gcd(num, num2)
        lcm_val = abs(num * num2) // gcd_val
        print(f"GCD: {gcd_val} | LCM: {lcm_val}")
    elif choice == '4':
        print(f"Is {num} a Perfect number? {is_perfect(num)}")