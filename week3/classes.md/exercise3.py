class Shape():
    def area(self):
        self.area=0

class Rectangle(Shape):
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def area(self):
        return self.width*self.lenght