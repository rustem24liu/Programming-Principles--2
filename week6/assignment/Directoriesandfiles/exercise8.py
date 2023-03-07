import os

f = r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5\RegEx\assignment\lab5\forweek6.txt'

if os.path.exists(f):
    os.remove(f)
    print(f'File {os.path.basename(f)} deleted!!!')