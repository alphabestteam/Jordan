import random
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = random.randint(1000, 9999)