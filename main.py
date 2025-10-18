from BankAccount import BankAccount

account =BankAccount("Amwaj")
menu = '''
1- Deposit
2- Withdraw
3- Check Balance
4- Account Holder Info
5- Exit
'''


print("=== Welcome to Simple Bank System ===")

while True:
    print(menu)
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            new_balance = account.deposit(amount)
            print(f"Deposit successful! New balance: {new_balance:.2f} SR")
        except ValueError as ve:
            print(f"Error: {ve}")
        input("")        

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            new_balance = account.withdraw(amount)
            print(f"Withdrawal successful! New balance: {new_balance:.2f} SR")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")
        input("")      

    elif choice == "3":
        print(f"Current balance: {account.get_balance():.2f} SR")
        input("")  

    elif choice == "4":
        print(f"Account holder: {account.get_account_holder()}")
        input("")  

    elif choice == "5":
        print("Thank you for using the Bank System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
