import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'

result = re.search('DC', s) # search -> return first finding string

print(result)
print(result[0])