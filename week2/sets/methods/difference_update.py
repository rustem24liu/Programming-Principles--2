x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)
y.difference_update(x)

print(y)

print(x)