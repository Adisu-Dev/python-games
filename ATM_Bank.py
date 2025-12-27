users = {
    "Adisu Dereje": ["0482", 10000],
    "Millan Nigusse": ["2345", 18000],
    "Tigst Amare": ["1254", 20000],
    "Kal Mengistu": ["4312", 15000],
}

print("\n\n WELCOME TO OUR BANKING SYSTEM")
name = input("Please Enter Your Name :  ")
# Check if user exists
if name in users:
    trials = 3
    access_granted = False
    while trials > 0:
        pin = input("Please Enter Your PIN:  ")
        if pin == users[name][0]:
            access_granted = True
            break
        else:
            trials -= 1
            print(f"Incorrect PIN. You have {trials} attempts left.")
    # Validate PIN
    if pin == users[name][0]:
        print(f"Welcome {name}!")
        while True:
            print("\nSelect an option:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Enter your choice (1-4):  ")
            if choice == "1":
                print(f"Your current balance is: ${users[name][1]}")
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    users[name][1] += amount
                    print(f"${amount} deposited successfully.")
                else:
                    print("Invalid amount. Please enter a positive number.")
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount <= users[name][1]:
                    users[name][1] -= amount
                    print(f"${amount} withdrawn successfully.")
                else:
                    print("Invalid amount or insufficient balance.")
            elif choice == "4":
                print("Thank you for using our banking system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Incorrect PIN. Access denied.")
else:
    print("User not found. Access denied.")
