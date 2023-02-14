
# НАСЛЕДОВАНИЕ
# add properties

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.secondname = lname
    def printname(self):
        print(self.firstname, self.secondname)
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduentyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.secondname, "to the class of", self.graduentyear)
res = Student("Rustem", "Temirgali", 2022)
res.welcome()

