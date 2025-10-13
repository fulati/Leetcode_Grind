class Bank:
    def __init__(self, balance: List[int]):
        # store as list; accounts are 1..n, we keep 0..n-1 internally
        self.bal = balance
        self.n = len(balance)

    def _valid(self, account: int) -> bool:
        # account is 1-indexed
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._valid(account1) or not self._valid(account2):
            return False
        i, j = account1 - 1, account2 - 1
        if self.bal[i] < money:
            return False
        self.bal[i] -= money
        self.bal[j] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        self.bal[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        i = account - 1
        if self.bal[i] < money:
            return False
        self.bal[i] -= money
        return True

        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)