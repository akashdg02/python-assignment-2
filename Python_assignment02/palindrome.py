def q17_palindrome():
    val = input("Enter word/number: ").lower()
    rev = val[::-1]
    print(f"Original: {val} | Reversed: {rev}")
    print("Result: PALINDROME" if val == rev else "Result: NOT PALINDROME")