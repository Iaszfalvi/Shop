class banking:

    def __init__(self) -> None:
        self.total = 5000

    def withdraw(self, amount):
        pass
    def deposit(self, amount):
        print("you just deposited: ", amount)
        self.total += amount
    def getTotal(self):
        print(self.total)

mybank = banking()
mybank.deposit(5000)
mybank.getTotal()

newbank = banking()
newbank.getTotal()