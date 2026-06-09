class ATM:
    def __init__(self):
        self.__pin = 6789
        self.balance = 162000
    def change_pin(self,old_pin):
        if old_pin == self.__pin:
            new_pin = int(input("Enter the new pin: "))
            self.__pin = new_pin
        else:
            print("Bro old password is wrong")
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount, pin):
        if self.__pin == pin:
            print("Correct Pin..Amount deducted..")
            self.balance -= amount
        else:
            print("Bro old password is wrong")
    def show_balance(self,pin):
        if self.__pin == pin:
            print("Your current balance: ",self.balance)

a1 = ATM()
a1.change_pin(6789)
a1.deposit(20000)
a1.withdraw(6789,10)
a1.withdraw(10,1234)
a1.show_balance(1234)
