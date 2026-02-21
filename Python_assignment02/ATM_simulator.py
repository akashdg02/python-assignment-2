def q10_atm_simulator():
    balance = 10000.0 # Initial balance [cite: 164]
    while True:
        print("\n1. Check Balance 2. Deposit 3. Withdraw 4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            print(f"Current Balance: ₹{balance}")
        elif choice == '2':
            amount = float(input("Enter deposit: "))
            balance += amount
            print(f"Updated Balance: ₹{balance}")
        elif choice == '3':
            amount = float(input("Enter withdrawal: "))
            # Rules: Sufficient balance and min ₹500 remains [cite: 165]
            if amount > balance:
                print("Error: Insufficient funds.")
            elif (balance - amount) < 500:
                print("Error: Minimum balance of ₹500 must remain.")
            else:
                balance -= amount
                print(f"Withdrawal successful! New Balance: ₹{balance}")
        elif choice == '4':
            print("Thank you for using the ATM.")