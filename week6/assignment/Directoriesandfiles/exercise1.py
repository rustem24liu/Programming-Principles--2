import os

for root, directories, files in os.walk(r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5'):
    print(root)
    for x in directories:
        print(x)
    for y in files:
        print(y)

# print([x.name for x in os.scandir(r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5')])


