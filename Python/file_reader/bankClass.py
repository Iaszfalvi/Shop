from gzip import FNAME

from setuptools import find_namespace_packages


class Bank(object):

    def __init__(self, f_name, l_name, balance, id) -> None:
        self.firstName = f_name 
        self.lastName = l_name 
        self.balance = balance
        self.id = id

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getBalance(self):
        return self.balance

    def getID(self):
        return self.id

