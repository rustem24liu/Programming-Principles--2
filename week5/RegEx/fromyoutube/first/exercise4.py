import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'

result = re.split('/', s)
result2 = re.split('/', s, maxsplit=4)

print(result)
print(result2)