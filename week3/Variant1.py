class Person():
    def __init__(self, name, nationallity):
        self.name = name
        self.nationallity = nationallity
    def printInfo(self):
        print('Name:', self.name)
        print('Nationallity:', self.nationallity)
    def setSurname(self, surname):
        self.surname = surname
    def getSurname(self):
        return self.surname
    
class Student(Person):
    def __init__(self, name, nationallity, id):
        super().__init__(name, nationallity)
        self.id = id
        
    def printInfo(self):
        super().printInfo()
        print('Id:', self.id)
    
        
        
stud = Student("Doka", "Kazakh", "22B030456")
print(stud.printInfo())