class Bank():
    def __init__(self,bal,owner) -> None:
        self.own=owner
        self.balance=bal
    def deposit(self):
        x=int(input())
        self.balance=self.balance+x
    def with_draw(self):
        x=int(input())
        if x>self.balance:
            print("You don't have enough money")
        else:
            self.balance=self.balance-x
