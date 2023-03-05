import re

with open(r"C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5\RegEx\assignment\lab5\info.txt", encoding="utf-8") as file:
    new = file.read()

result = re.findall(r'.*a.*b{2,3}', new)
# res = re.findall(r'HYDRO', new)

print(result)
# print(res)