thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
[print(x) for x in thislist]
for x in range(len(thislist)):
    print(thislist[x])

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1