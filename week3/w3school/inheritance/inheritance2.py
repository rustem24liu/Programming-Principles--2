# НАСЛЕДОВАНИЕ

class Person:
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
    def printname(self):
        print(self.fname, self.lname)
class Student(Person):
    def __init__(self,firstname, lastname):
        Person.__init__(self, firstname,lastname)



res2 = Student("Mike", "Tayson")
res2.printname()
# res = Person("Rustem", "Temirgali")
# res.printname()