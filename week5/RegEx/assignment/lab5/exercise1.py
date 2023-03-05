import re

with open(r"C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5\RegEx\assignment\lab5\info.txt", encoding="utf-8") as file:
    new = file.read()


x = re.findall(r'.*a.*b.*', new)
print(x)
