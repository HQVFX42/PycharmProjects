class BankAccount:
    def __init__(self, balance, name, number):
        self.balance = balance
        self.name = name
        self.number = number
    def withdraw(self, money):
        self.balance -= money
    def deposit(self, money):
        self.balance += money
    def __str__(self):
        return "계좌번호 : " + self.number +"\n계좌잔액 : "+str(self.balance)

class SavingAccount(BankAccount):
    def __init__(self, balance, name, number, interest_rate):
        super().__init__(balance,name,number)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += self.balance*self.interest_rate
    def __str__(self):
        return super().__str__()+"\n이자율 : "+ str(self.interest_rate)

class CheckinAccount(BankAccount):
    def __init__(self, balance, name, number, withdraw_charge):
        super().__init__(balance,name,number)
        self.withdraw_charge = withdraw_charge
    def withdraw(self, money):
        super().withdraw(money)
        self.balance -= self.withdraw_charge

    def __str__(self):
        return super().__str__()+"\n수수료 : "+str(self.withdraw_charge)

s = SavingAccount(1000000,"장인호","010-112-119",0.1)
print(s)
s.add_interest()
print(s)
c = CheckinAccount(1000000,"장인호","010-112-119",1000)
c.withdraw(10000)
print(c)