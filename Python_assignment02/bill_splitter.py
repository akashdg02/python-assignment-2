def q5_bill_splitter():
    try:
        # Get inputs [cite: 102]
        total_bill = float(input("Enter total bill: "))
        people = int(input("Number of people: "))
        tax_perc = float(input("Tax percentage: "))
        tip_perc = float(input("Tip percentage: "))
        
        # Calculations [cite: 103]
        tax_amount = total_bill * (tax_perc / 100)
        after_tax = total_bill + tax_amount
        tip_amount = total_bill * (tip_perc / 100)
        grand_total = after_tax + tip_amount
        per_person = grand_total / people if people > 0 else grand_total
        
        print("\n=== BILL BREAKDOWN ===")
        print(f"Subtotal: ₹{total_bill:.2f}")
        print(f"Tax ({tax_perc}%): ₹{tax_amount:.2f}")
        print(f"After tax: ₹{after_tax:.2f}")
        print(f"Tip ({tip_perc}%): ₹{tip_amount:.2f}")
        print(f"Total: ₹{grand_total:.2f}")
        print(f"Per person: ₹{per_person:.2f}")
    except ValueError:
        print("Invalid numeric input.")