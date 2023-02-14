# НАСЛЕДОВАНИЕ

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)

#Use the Person class to create an object, and then execute the printname method:
res = Person("Rustem", "Temirgali")
res.printname()