def q12_multi_table():
    num = int(input("Enter number: "))
    limit = int(input("Enter range: "))
    print(f"Multiplication Table of {num}:")
    for i in range(1, limit + 1):
        print(f"{num} x {i} = {num * i}") # [cite: 173]