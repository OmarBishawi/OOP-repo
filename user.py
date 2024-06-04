class user:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def make_withdrawal(self,amount):
        if amount>self.balance:
            print("insufficent funds .withdrawal canceled")
        else:
            self.balance -= amount

    def display_user_balance(self):
        print(f"user: {self.name}, balance :${self.balance}")        

    def transfer_money(self,other_user,amount):
        if amount>self.balance:
            print("insufficent funds. withdrawal canceled")
        else:
            self.balance -= amount
            other_user.balance +=amount

user1 = user("omar",1000)
user2 = user("bob",500)
user1.make_withdrawal(200)
user1.display_user_balance()
user2.make_withdrawal(100)
user2.display_user_balance()
user1.transfer_money(user2,300)
user1.display_user_balance()
user2.display_user_balance()

    
