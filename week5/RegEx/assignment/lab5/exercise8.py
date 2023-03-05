import re

with open(r"C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5\RegEx\assignment\lab5\info.txt", encoding="utf-8") as file:
    result = re.findall(r'[A-Z][^A-Z]*', file.read() )
    print(result)