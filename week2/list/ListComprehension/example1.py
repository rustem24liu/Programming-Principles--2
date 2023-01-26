fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
newlist2 = list(())

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
for y in fruits:
    if "e" in y:
        newlist2.append(y)
print(newlist2)