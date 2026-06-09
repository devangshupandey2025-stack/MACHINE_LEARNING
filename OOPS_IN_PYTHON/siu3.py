class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Amount Deposited")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Withdrawed...Please collect")

    def show_balance(self):
        print("Account Holder\tBank Balance")
        print(self.name,"\t\t",self.balance)

acc1 = BankAccount("Dev",25000)
while(True):
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        amt = int(input("Enter Amount to be Deposited: "))
        acc1.deposit(amt)
    elif choice == 2:
        amt = int(input("Enter Amount to be Withdrawed: "))
        acc1.withdraw(amt)
    elif choice == 3:
        acc1.show_balance()
    elif choice == 4:
        acc1.show_balance()
        break
