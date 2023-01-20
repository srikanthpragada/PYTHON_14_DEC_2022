class BalanceError(Exception):
    def __init__(self, balance, amount):
        self.message = f"Insufficient balance {balance} for withdraw of {amount}"

    def __str__(self):
        return self.message


class Account:
    def __init__(self, acno, customer, balance=0):
        # object attributes
        self.acno = acno
        self.customer = customer
        # private attribute
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise BalanceError(self.__balance, amount)

        self.__balance -= amount

    def getbalance(self):
        return self.__balance


# a1 = Account(1, "Rogers", 10000)
# print(a1.__dict__)
# print(a1.__balance)
# print(a1._Account__balance)
# a1.deposit(10000)
# a1.withdraw(5000)
# print(a1.getbalance())

a2 = Account(2, "David")
try:
    a2.withdraw(10000)
except BalanceError as ex:
    print("Error : ", ex)



