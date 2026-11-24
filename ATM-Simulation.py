print ("Welcome to the ATM Simulation Program!")
balance = 5000
while True:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Please select an option (1-4): ")
    if choice == "1":
        print(f"Your current balance is: ${balance}")
    elif choice == "2":
        try:
            deposit_amount = float(input("Enter the amount to deposit: "))
            if deposit_amount > 0:
             balance += deposit_amount
             print(f"Deposit successful. New balance: ${balance}")
            else:
             print("Invalid amount. Please enter an amount greater than zero.") 
        except ValueError:
          print("Invalid input. Please enter a valid number.")
        continue
    elif choice == "3":
        try:
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            if withdraw_amount <= 0:
               print("Invalid withdrawal amount.")
            elif withdraw_amount > balance:
                print("Insufficient funds.")
            else:
                balance -= withdraw_amount
                print(f"Withdrawal successful! New balance: ${balance}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        continue
    elif choice == "4":
        print("Thank you for using the ATM Simulation Program!")
        break
    else:
        print("Invalid option. Please try again.")