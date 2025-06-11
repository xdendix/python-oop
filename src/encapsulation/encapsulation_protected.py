class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def _get_balance(self):  # Protected method
        return self._balance  # Accessing protected attribute within the class

    def display(self):
        return self._get_balance()  # Accessing protected method within the class


account = BankAccount(1000)
print(account.display())
print(account._balance)
