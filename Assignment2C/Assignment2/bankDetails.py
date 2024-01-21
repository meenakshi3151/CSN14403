class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs{amount}. New balance: Rs{self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw Rs{amount}. New balance: Rs{self.balance}")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")
    
    def display_info(self):
        print(f"Account Information:\nAccount Number: {self.account_number}\nOwner Name: {self.owner_name}\nBalance: Rs{self.balance}")

account1 = BankAccount(account_number=input("Enter your account number: "), owner_name=input("Enter your name: "), initial_balance=int(input("Enter your initial balance: ")))
account1.deposit(int(input("Enter amount to deposit: ")))
account1.withdraw(int(input("Enter amount to withdraw: ")))
account1.display_info()
