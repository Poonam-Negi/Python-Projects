# A simple banking system
# Features:
# - Deposit money
# - Show balance
# - Withdraw money
# - Exit

# Function to display the current balance
def show_balance(balance):
    print("*********************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************")

# Function to handle deposits
def deposit():
    print("*********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("*********************")
    # Check if the deposit amount is valid
    if amount < 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0  # Return 0 if the amount is invalid
    else:
        print("*********************")
        print(f"Successfully deposited ${amount:.2f}")
        print("*********************")
        return amount  # Return the valid deposit amount

# Function to handle withdrawals
def withdraw(balance):
    print("*********************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("*********************")
    # Check if withdrawal amount exceeds balance
    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0  # Return 0 if funds are insufficient
    # Check if withdrawal amount is negative
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0  # Return 0 for invalid input
    else:
        print("*********************")
        print(f"Successfully withdrew ${amount:.2f}")
        print("*********************")
        return amount  # Return the valid withdrawal amount

# Main function to run the banking system
def main():
    balance = 0  # Initialize balance to zero
    is_running = True  # Flag to keep the program running

    # Loop until the user chooses to exit
    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")
        choice = input("Enter your choice (1-4): ")

        # Handle user choice
        if choice == '1':
            show_balance(balance)  # Display balance
        elif choice == '2':
            balance += deposit()  # Add deposit to balance
        elif choice == '3':
            balance -= withdraw(balance)  # Deduct withdrawal from balance
        elif choice == '4':
            is_running = False  # Exit the loop
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")

    # Program termination message
    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

# Entry point of the program
if __name__ == '__main__':
    main()
