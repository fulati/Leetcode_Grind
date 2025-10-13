class Bank:
    def __init__(self, balance: List[int]):
        # balance[i] stores the money in account (i+1)
        self.bal = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # account numbers are 1-indexed (1 to n)
        if account1 < 1 or account1 > self.n or account2 < 1 or account2 > self.n:
            return False
        # convert to 0-index for internal list access
        i, j = account1 - 1, account2 - 1
        # check enough money
        if self.bal[i] < money:
            return False
        # perform transfer
        self.bal[i] -= money
        self.bal[j] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # check account validity
        if account < 1 or account > self.n:
            return False
        self.bal[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        idx = account - 1
        if self.bal[idx] < money:
            return False
        self.bal[idx] -= money
        return True


        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)