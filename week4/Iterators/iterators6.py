class Mynumber:
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < 99:
            x = self.a
            self.a+=5
            return x
        else:
            raise StopIteration

myclass = Mynumber()
myiter = (iter(myclass))

for x in myiter:
    print(x, end = ' ')