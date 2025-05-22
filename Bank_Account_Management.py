class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0.0): # Here self is object.account_number, account_holder, balance inputs to the constructor
        self.__account_number = account_number # These inputs are stored in the object using self.__attribute_name
        self.__account_holder = account_holder # These inputs are stored in the object using self.__attribute_name
        self.__balance = balance # These inputs are stored in the object using self.__attribute_name
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Amount: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit Amount")
            
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw Amount: {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient Balance")
            
# To access a private variable(self.__balance) which have double underscore)) from outside, you'd have to use a getter method
    def get_balance(self): # get() → Read(Access) the value
        return self.__balance
        
    def display_info(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")
        
# Derived class for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.03):
        super().__init__(account_number, account_holder, balance) # super() - it uses to derive attributes for account_number,account_holder,balance from ParentClass(BankAccount)
        self.interest_rate = interest_rate
        
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate # you cant access private variable self.__balance you use get method to return balance(self.get_balance())
        self.deposit(interest)
        print(f"Interest of ₹{interest:.2f} applied.")
    
# Derived class for Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit = 5000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            self._BankAccount__balance = new_balance  
            """You can't write self.__balance = new_balance, because it is a private attribute in ParentClass so in
            sub classes(Savings,Current account) python internally renames it to _BankAccount__balance to protect it.
            """ 
            print(f"Withdraw Amount: {amount}. New Balance: {new_balance}")
        else:
            print(f"Overdraft limit exceeded or invalid amount.")
            
# Main Interactive Program
def main():
    print("_____Welcome to Bank Management System!_____")
    account_type = input("Select Account Type(Savings/Current): ").strip().lower()
    acc_num = input("Enter Account Number: ")
    acc_holder = input("Enter Account holder name: ")
    initial_balance = float(input("Enter initial balance: "))
    
    if account_type == "savings":
        acc = SavingsAccount(acc_num, acc_holder, initial_balance)
    elif account_type == "current":
        acc = CurrentAccount(acc_num, acc_holder, initial_balance)
    else:
        print("Invalid account type")
        return
    
    while True:
        print("--Choose an operation")
        print("1. Display account info: ")
        print("2. Deposit ")
        print("3. Withdraw ")
        if account_type == 'savings':
            print("4. Apply Interest ")
            choice = input("Select Choice(1/2/3/4/5): ")
        else:
            choice = input("Select Choice(1/2/3/5): ")
        print("5. Exit")
        
        if choice == '1':
            acc.display_info()
        elif choice == '2':
            amount = float(input("Enter Amount: "))
            acc.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter Amount:"))
            acc.withdraw(amount)
        elif choice == '4' and account_type == 'savings':
            acc.apply_interest()
        elif choice == '5':
            print("Exiting Bank Management System")
            break
        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    main()