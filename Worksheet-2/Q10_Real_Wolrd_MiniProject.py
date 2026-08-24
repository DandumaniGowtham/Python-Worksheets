class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def check_balance(self):
        print("Current Balance:", self.balance)

# Creating account object
account = BankAccount(101, "Gowtham", 5000)

while True:
    print("\n Bank Menu ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        print("Exited")
        break

    else:
        print("Invalid choice.")