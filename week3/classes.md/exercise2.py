class Shape():
    def area(self):
        self.length = 0
class Square(Shape):
    def __init__(self, length):
        self.length1 = length
        self.length2 = length
    def area(self):
        print(self.length1 * self.length2)

x = Square(9)
x.area()