def q9_ticket_pricing():
    age = int(input("Age: "))
    day = input("Day of week: ").lower()
    num = int(input("Number of tickets: "))
    
    # Age brackets [cite: 161]
    if age < 3: base = 0
    elif 3 <= age <= 12: base = 150
    elif 13 <= age <= 59: base = 300
    else: base = 200
    
    # Weekend discount [cite: 161]
    discount = 0.20 if day in ['friday', 'saturday', 'sunday'] else 0.0
    
    final_price = base * (1 - discount)
    print(f"Base: ₹{base} | Discount: {discount*100}% | Total: ₹{final_price * num}")