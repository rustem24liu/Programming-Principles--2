# The __str__() contrlos what hsould be returned when the class object is represented as a string

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)