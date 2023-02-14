class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def show(self,):
        print(self.x,self.y)
    
    def move(self):
        x1=int(input())
        y1=int(input())
        self.x=x1
        self.y=y1
    
    def dist(self):
        x1=int(input())
        y1=int(input())
        print(self.x+x1,self.y+y1)

x=int(input())
y=int(input())

w=Point(x,y)
w.move()
w.show()
w.dist()
