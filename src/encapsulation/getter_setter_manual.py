class BankAccount:
    def __init__(self, name, balance):  # constructor
        self.__name = name  # private attribute
        self.__balance = balance  # private attribute

    def get_balance(self):  # getter method
        return self.__balance

    def set_balance(self, amount):  # setter method
        if amount >= self.__balance:
            print("saldo tidak cukup")
            return

        self.__balance = amount


account = BankAccount("Dendi", 3000)  # create an instance of BankAccount
print(f"saldo saat ini {account.get_balance()}")  # get balance using getter method

account.set_balance(2000)  # set balance using setter method
print(f"saldo saat ini {account.get_balance()}")  # get balance using getter method
