import re

s = 'Привет! Как дела? , А у  меня все хорошо'

result = re.findall(r'[БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ]\w*', s)

print(result)
  