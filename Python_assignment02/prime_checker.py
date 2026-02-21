def q15_prime_checker():
    def is_p(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    
    num = int(input("Enter number: "))
    print(f"{num} is PRIME" if is_p(num) else "NOT PRIME")
    
    # Range check [cite: 187]
    s, e = int(input("Start range: ")), int(input("End range: "))
    print(f"Primes: {[x for x in range(s, e+1) if is_p(x)]}")