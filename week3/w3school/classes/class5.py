# Insert a function that prints a greeting, and execute it on the p1 object:

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfinc(self):
        print("Hello my name is "+self.name)
res = Person("Rustem", 17)
res.myfinc()