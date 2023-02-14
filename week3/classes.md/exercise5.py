class MyBank():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        depositi = int(input("Your deposit? "))
        self.balance += depositi
    def with_draw(self):
        drawel = int(input("How many money want withdraw? "))
        if drawel > self.balance:
            print("You dont have enough balance for withdraw!!!")
        else:
            self.balance -= drawel
        print(self.owner, "your balance is:", self.balance)

x = MyBank("Arnold Arnur", 2000)
x.deposit()
x.with_draw()
