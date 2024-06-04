class bank_account :
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        
    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -=amount
            return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

bank_account1=bank_account(5000,.02)   
bank_account2=bank_account(2000,.01)
bank_account1.deposit(500).deposit(400).deposit(300).withdraw(2000).display_account_info()
bank_account2.deposit(1000).deposit(2000).withdraw(3000).withdraw(100).withdraw(200).withdraw(300).yield_interest().display_account_info()