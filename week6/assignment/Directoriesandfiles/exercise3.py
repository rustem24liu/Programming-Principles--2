import os

f = r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5\RegEx\assignment\lab5\info.txt'

if os.path.exists(f):
    if os.path.isdir(f):
        print(os.path.dirname(f))
    else:
        print(os.path.basename(f))
else:
    print("I could not find directory like this")
        