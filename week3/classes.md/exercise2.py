class Shape():
    def area(self):
        self.length = 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length*self.length)

x = Square(9)    
x.area()