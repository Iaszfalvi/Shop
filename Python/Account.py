class Account(object):

    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.account_number = account_number
        self.balance = initial_amount
        

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getInfo(self):
        print(self.name, self.account_number, self.balance)

    def getName(self):
        return self.name

    def getAccount(self):
        pass

    def getBalance(self):
        pass