class Shape():
    def area(self):
        self.length = 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length*self.length)
class Rectangle(Square):
    def __init__(self, length, width):
        self.len1 = length
        self.len2 = width
    def printeq(self):
        print(self.len1*self.len2)

x = Rectangle(9, 2)
x.printeq()