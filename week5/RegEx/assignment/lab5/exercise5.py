import re

with open(r"C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5\RegEx\assignment\lab5\info.txt",encoding="utf-8") as file:
    for new in file:
        if re.search(r'^a.*b$' , new):
            print(new, end ='')
    