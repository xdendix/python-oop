class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def __get_balance(self):  # Private method
        return self.__balance  # Accessing private attribute within the class

    def display(self):
        return self.__get_balance()  # Accessing private method within the class


account = BankAccount(1000)
print(account.display())
