class Account:
    def __init__(self,id=0,balance=100.0,annualInterestRate=0.0):
        self.id =id
        self.balance =balance
        self.annualInterestRate =annualInterestRate

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate
    
    def setId(self, id):
        self.id = id

    def setBalance(self, balance):
        self.balance = balance

    def setAnnualInterestRate(self, annualInterestRate):
        self.annualInterestRate = annualInterestRate

    # Method to get the monthly interest rate
    def getMonthlyInterestRate(self):
        return self.annualInterestRate/12

    # Method to calculate the monthly interest
    def getMonthlyInterest(self):
        return self.balance*self.getMonthlyInterestRate()/100

    # Method to withdraw a specified amount
    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient balance in this account")
        else:
            self.balance-=amount

    def deposit(self, amount):
        self.balance+=amount

acc = Account(id=1122, balance=20000, annualInterestRate=4.5)
acc.withdraw(2500)
acc.deposit(3000)
print("The ID:", acc.getId())
print("Balance:",acc.getBalance())
print("Monthly interest rate:", acc.getMonthlyInterestRate())
print("Monthly interest:", acc.getMonthlyInterest())
