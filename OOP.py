class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Депозит должен быть положительный")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма вывода должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма вывода должна быть положительной")
        self._BankAccount__balance -= amount 


account = SavingsAccount("Артем Лукин")

account.deposit(500)

account.withdraw(100)

account.apply_interest()

print(account.get_balance())  # Выведет: 420.0 (400 + 5% = 420)