class BankAccount:
    def __init__(self, name, balance):  # constructor
        self.__name = name  # private attribute
        self.__balance = balance  # private attribute

    @property  # property decorator
    def balance(self):  # getter method
        return self.__balance

    @balance.setter  # setter method
    def balance(self, amount):  # setter method
        if amount >= self.__balance:
            print("saldo tidak cukup")
            return

        self.__balance = amount


account = BankAccount("Dendi", 3000)  # create an instance of BankAccount
print(f"saldo saat ini {account.balance}")  # get balance using getter method

account.balance = 1000  # set balance using setter method
print(f"saldo saat ini {account.balance}")  # get balance using getter method
