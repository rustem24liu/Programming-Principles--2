class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("Points:")
        print(self.x, self.y)
    def move(self):
        newx = int(input("print new 'x'\n"))
        newy = int(input("print new 'y\n"))
        self.x = newx
        self.y = newy
    def dist(self):
        distance = abs(self.x-self.y)
        print("The distance between", self.x, "and", self.y, "is:", distance)
      

x = Point(5, 11)
x.show()
x.move()
x.dist()