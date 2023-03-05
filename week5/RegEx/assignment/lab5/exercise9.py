import re

with open(r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5\RegEx\assignment\lab5\info.txt', encoding="utf-8") as file:
    x = re.findall(r"\b[A-Z]\w+",file.read())
    for i in ((x)):
        for j in range(len(i)):
            print(i[j], end = ' ')
    