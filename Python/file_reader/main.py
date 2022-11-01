from bankClass import Bank
from readfile import Reader

def generateBankObject():

    customer_array = Reader().readFile("customers.txt")
    bank_array = []

    for c in customer_array:
        bank_array.append(Bank(c[0], c[1], c[2], c[3]))
     
    return bank_array
    

bank = generateBankObject()

for e in bank:
    print(e.getLastName(), e.getFirstName())
   