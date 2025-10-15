class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.n = len(balance) 
    
    def transfer(self, acc1, acc2, money):
        if acc1 < 1 or acc1 > self.n or acc2 < 1 or acc2 > self.n:
            return False
        
        if self.balance[acc1 - 1] < money:
            return False
        
        self.balance[acc1 - 1] -= money
        self.balance[acc2 - 1] += money
        return True
    
    def deposit(self, acc, money):
        if acc < 1 or acc > self.n:
            return False

        self.balance[acc - 1] += money
        return True

    def withdraw(self, acc, money):
        if acc < 1 or acc > self.n:
            return False
        
        if self.balance[acc - 1] < money:
            return False
        
        self.balance[acc - 1] -= money
        return True