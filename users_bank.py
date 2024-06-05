class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self


class User:
    def __init__(self, balance, interest_rate):
        self.account = BankAccount(balance, interest_rate)  # association with BankAccount

    def deposit(self, amount):
        self.account.deposit(amount)  # calls BankAccount's deposit method
        return self

    def withdraw(self, amount):
        self.account.withdraw(amount)  # calls BankAccount's withdraw method
        return self

    def display_account_info(self):
        self.account.display_account_info()  # calls BankAccount's display_account_info method
        return self

    def yield_interest(self):
        self.account.yield_interest()  # calls BankAccount's yield_interest method
        return self


# Test the updated classes
bank_account1 = User(5000, 0.02)
bank_account2 = User(2000, 0.01)

bank_account1.deposit(500).deposit(400).deposit(300).withdraw(2000).display_account_info()
bank_account2.deposit(1000).deposit(2000).withdraw(3000).withdraw(100).withdraw(200).withdraw(300).yield_interest().display_account_info()
