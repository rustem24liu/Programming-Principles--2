
# НАСЛЕДОВАНИЕ
# function super()

class Person:
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
    def printname(self):
        print(self.fname, self.lname)
class Student(Person):
    def __init__(self,firstname, lastname):
        super().__init__(self, firstname, lastname)

