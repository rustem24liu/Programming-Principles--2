import re

with open(r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5\RegEx\assignment\lab5\info.txt', encoding='utf-8') as file:
    result = re.sub(r'_([a-z])', lambda match : match.group(1).upper(), file.read())
    print(result)
