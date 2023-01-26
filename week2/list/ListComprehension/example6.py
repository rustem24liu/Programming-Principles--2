fruits = ["apple", "banana", "cherry"]

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

newlist2 = [y if y != "cherry" else "new eda" for y in fruits]
print(newlist2)