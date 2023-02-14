# Use the words mysillyobject and abc instead of self:

class Person():
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello, my name is "+abc.name)
res = Person("Rustem", 17)
res.myfunc()
res.age = 18
print(res.age)