import re

with open(r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5\RegEx\assignment\lab5\info.txt', encoding="utf-8") as file:
    new = file.read()

result = re.findall(r'.*[a-z]_[a-z].*', new) #! we can also wtrite without '+'
print(result)